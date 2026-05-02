from typing import Callable
from joho.core.normalizers.base_normalizer import BaseNormalizer
from joho.core.normalizers.anilist_normalizer import AnilistNormalizer
from joho.core.normalizers.jikan_normalizer import JikanNormalizer
from joho.core.models.protocols import FetchersProtocol
from joho.core.constants import DATA_SOURCES, VALID_DATA_SOURCES
from joho.core.exceptions import InvalidDataSource


def create_normalizer(
    source: DATA_SOURCES, fetcher: FetchersProtocol
) -> BaseNormalizer:
    normalizer_map: dict[str, Callable[[FetchersProtocol], BaseNormalizer]] = {
        "anilist": AnilistNormalizer,
        "jikan": JikanNormalizer,
    }
    cls = normalizer_map.get(source)
    if cls is None:
        raise InvalidDataSource(
            f"Invalid data source provided ({source}), expected ({VALID_DATA_SOURCES})"
        )
    return cls(fetcher)
