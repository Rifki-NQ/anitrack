from jikanpy import Jikan, APIException
from typing import Any
from core.fetchers.base_fetcher import FetchData, check_internet
from core.exceptions import JikanError

class FetchJikan(FetchData):
    def __init__(self) -> None:
        self.jikan = Jikan()
        
    def fetch_data_by_title(self, anime_title: str) -> list[dict[str, Any]]:
        anime_data = self._search_anime(anime_title)
        return anime_data
    
    @check_internet
    def fetch_data_by_id(self, anime_id: int) -> dict[str, Any]:
        try:
            return self.jikan.anime(anime_id)["data"]
        except APIException as e:
            raise JikanError(f"Error: requested anime not found! status code: {e.status_code}")
    
    @check_internet
    def _search_anime(self, anime_title: str) -> list[dict[str, Any]]:
        try:
            data = self.jikan.search(search_type="anime", query=anime_title)["data"]
        except APIException as e:
            message = e.error_json["message"] if e.error_json is not None else None
            raise JikanError(f"Error: {message}, status code: {e.status_code}")
        if not data:
            raise JikanError("Error: requested anime not found!")
        return data