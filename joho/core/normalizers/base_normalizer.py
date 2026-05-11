from typing import Any, Callable
from abc import ABC, abstractmethod
from joho.core.models.anime_model import AnimeDataModel


def batch_to_anime_model(
    raw_data_list: list[dict[str, Any]],
    max_entry: int | None,
    anime_model_converter: Callable[[dict[str, Any]], AnimeDataModel],
) -> list[AnimeDataModel]:
    """convert list of raw entry data dict into list of AnimeDataModel"""
    model_data_list: list[AnimeDataModel] = []
    for entry_num, data in enumerate(raw_data_list, 1):
        # inclusive for max_entry value
        if max_entry is not None and entry_num > max_entry:
            break
        model_data_list.append(anime_model_converter(data))
    return model_data_list


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
