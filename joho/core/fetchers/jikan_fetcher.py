import requests
from typing import Any
from joho.core.fetchers.base_fetcher import FetchData, check_internet
from joho.core.exceptions import AppConnectionError


class FetchJikan(FetchData):
    BASE_URL = "https://api.jikan.moe/v4/anime"
    SORT_MAP = {
        "rating": "score",
        "popularity": "popularity",
        "relevance": "title",
        "newest": "start_date",
        "oldest": "end_date",
    }
    DEFAULT_SORT = "relevance"

    def fetch_data_by_title(
        self, anime_title: str, sort: str | None
    ) -> list[dict[str, Any]]:
        sort = sort if sort is not None else self.DEFAULT_SORT
        params: dict[str, str | int] = {
            "q": anime_title,
            "page": 1,
            "order_by": self.SORT_MAP[sort],
            "sort": "desc",
        }
        data = self._query_anime(self.BASE_URL, params)
        return data.json()["data"]

    def fetch_data_by_id(self, anime_id: int) -> dict[str, Any]:
        base_url = f"{self.BASE_URL}/{anime_id}"
        data = self._query_anime(base_url)
        return data.json()["data"]

    @check_internet
    def _query_anime(
        self, base_url: str, params: dict[str, str | int] | None = None
    ) -> requests.Response:
        try:
            response = requests.get(base_url, params=params)
        except requests.ConnectionError as e:
            raise AppConnectionError(f"Connection error occured: {e}")
        return response
