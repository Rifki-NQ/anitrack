import requests
from abc import ABC, abstractmethod
from typing import Literal, get_args, Any
from core.exceptions import InvalidDataSource

class FetchData(ABC):
    DATA_SOURCES = Literal["anilist"]
    VALID_DATA_SOURCES = get_args(DATA_SOURCES)
    
    @staticmethod
    def create_fetcher(data_source: DATA_SOURCES) -> FetchData:
        if data_source == "anilist":
            return FetchAnilist()
        else:
            raise InvalidDataSource(f"Invalid data source provided ({data_source}), expected ({FetchData.VALID_DATA_SOURCES})")
        
    @abstractmethod
    def fetch_data(self, anime_title: str) -> dict[str, Any]:
        pass
    
    def _request(self, url: str, query: str, variables: dict[str, str]) -> requests.Response:
        response = requests.post(url, json={"query": query, "variables": variables})
        return response
    
class FetchAnilist(FetchData):
    BASE_URL = "https://graphql.anilist.co"
    QUERY = """
    query ($search: String) {
        Media (search: $search, type: ANIME) {
            id
            title {
                english
                romaji
            }
            averageScore
            episodes
            genres
        }
    }
    """
    
    def fetch_data(self, anime_title: str) -> dict[str, Any]:
        data = self._request(url=self.BASE_URL, query=self.QUERY, variables={"search": anime_title})
        return data.json()