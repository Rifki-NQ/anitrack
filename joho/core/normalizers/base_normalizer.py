from abc import ABC, abstractmethod
from joho.core.models.anime_model import AnimeDataModel


class BaseNormalizer(ABC):
    @abstractmethod
    async def get_anime_by_title(
        self, anime_title: str, sort: str, entry_index: int | None = None
    ) -> AnimeDataModel:
        pass

    @abstractmethod
    async def get_anime_by_id(
        self,
        anime_id: int,
    ) -> AnimeDataModel:
        pass

    @abstractmethod
    async def get_all_anime_by_title(
        self, anime_title: str, sort: str, max_entry: int | None = None
    ) -> list[AnimeDataModel]:
        pass
