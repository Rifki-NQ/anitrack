from abc import ABC, abstractmethod
from typing import Literal, get_args
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
    def fetch_data(self, query: str):
        pass
    
class FetchAnilist(FetchData):
    BASE_URL = "https://graphql.anilist.co"
    
    def fetch_data(self, query: str):
        pass