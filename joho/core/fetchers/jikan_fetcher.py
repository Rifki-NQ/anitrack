import requests
from typing import Any
from joho.core.fetchers.base_fetcher import FetchData, check_internet
from joho.core.exceptions import AppConnectionError, JikanError


class FetchJikan(FetchData):
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

    def fetch_data_by_title(
        self, anime_title: str, sort: str
    ) -> list[dict[str, Any]]:
        params: dict[str, str | int | None] = {
            "q": anime_title,
            "page": 1,
            "order_by": self.SORT_MAP[sort],
            "sort": "desc",
        }
        data = self._query_anime(self.BASE_URL, params)
        json_data = data.json()["data"]
        if not json_data:
            raise JikanError("Error: requested anime not found!")
        return json_data

    def fetch_data_by_id(self, anime_id: int) -> dict[str, Any]:
        base_url = f"{self.BASE_URL}/{anime_id}"
        data = self._query_anime(base_url)
        json_data = data.json()["data"]
        if not json_data:
            raise JikanError("Error: requested anime not found!")
        return json_data

    @check_internet
    def _query_anime(
        self, base_url: str, params: dict[str, str | int | None] | None = None
    ) -> requests.Response:
        try:
            response = requests.get(base_url, params=params)
        except requests.ConnectionError as e:
            raise AppConnectionError(f"Connection error occured: {e}")
        return response
