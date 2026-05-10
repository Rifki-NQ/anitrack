from typing import Protocol, Any
from joho.core.models.anime_model import AnimeDataModel


class FetchersProtocol(Protocol):
    async def fetch_data_by_title(
        self, anime_title: str, sort: str
    ) -> list[dict[str, Any]]: ...

    async def fetch_data_by_id(self, anime_id: int) -> dict[str, Any]: ...


class NormalizerProtocol(Protocol):
    async def get_anime_by_title(
        self, anime_title: str, sort: str, entry_index: int | None = None
    ) -> AnimeDataModel: ...

    async def get_anime_by_id(self, anime_id: int) -> AnimeDataModel: ...

    async def get_all_anime_by_title(
        self, anime_title: str, sort: str, max_entry: int | None = None
    ) -> list[AnimeDataModel]: ...
