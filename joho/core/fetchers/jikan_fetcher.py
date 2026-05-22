import httpx
from typing import Any, cast
from joho.core.fetchers.base_fetcher import FetchData
from joho.core.exceptions import AppConnectionError, AnimeNotFoundError
from joho.core.constants import GLOBAL_TIMEOUT


class FetchJikan(FetchData):
    def __init__(self, client: httpx.AsyncClient) -> None:
        super().__init__(client)

    BASE_URL = "https://api.jikan.moe/v4/anime"
    # default sort is relevance (based on constants.py value)
    # relevance = None, since jikan order_by is not working properly currently
    SORT_MAP: dict[str, str | None] = {
        "rating": "score",
        "popularity": "popularity",
        "relevance": None,
        "newest": "start_date",
        "oldest": "end_date",
    }

    async def fetch_data_by_title(
        self, anime_title: str, sort: str
    ) -> list[dict[str, Any]]:
        params: dict[str, str | int | None] = {
            "q": anime_title,
            "page": 1,
            "order_by": self.SORT_MAP[sort],
            "sort": "desc",
        }
        data = await self._query_anime(self.BASE_URL, params)
        json_data = data.json()["data"]
        if not json_data:
            raise AnimeNotFoundError("jikan", anime_title)
        return cast(list[dict[str, Any]], json_data)

    async def fetch_data_by_id(self, anime_id: int) -> dict[str, Any]:
        base_url = f"{self.BASE_URL}/{anime_id}"
        data = await self._query_anime(base_url)
        json_data = data.json()["data"]
        if not json_data:
            raise AnimeNotFoundError("jikan", anime_id)
        return cast(dict[str, Any], json_data)

    async def _query_anime(
        self, base_url: str, params: dict[str, str | int | None] | None = None
    ) -> httpx.Response:
        try:
            response = await self.client.get(
                base_url, params=params, timeout=GLOBAL_TIMEOUT
            )
            response.raise_for_status()
            return response
        except httpx.RequestError as e:
            raise AppConnectionError(f"Connection error occurred: {e}") from e
        except httpx.HTTPStatusError as e:
            raise AppConnectionError(
                f"API returned: {e.response.status_code} ({e})"
            ) from e
