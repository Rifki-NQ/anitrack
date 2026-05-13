from abc import ABC, abstractmethod
from typing import Any
from httpx import AsyncClient


class FetchData(ABC):
    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    @abstractmethod
    async def fetch_data_by_title(
        self, anime_title: str, sort: str
    ) -> list[dict[Any, Any]]:
        pass

    @abstractmethod
    async def fetch_data_by_id(self, anime_id: int) -> dict[Any, Any]:
        pass
