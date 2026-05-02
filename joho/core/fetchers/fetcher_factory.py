from joho.core.fetchers.base_fetcher import FetchData
from joho.core.fetchers.anilist_fetcher import FetchAnilist
from joho.core.fetchers.jikan_fetcher import FetchJikan
from joho.core.constants import DATA_SOURCES, VALID_DATA_SOURCES
from joho.core.exceptions import InvalidDataSource


def create_fetcher(data_source: DATA_SOURCES) -> FetchData:
    source_map: dict[str, type[FetchData]] = {
        "anilist": FetchAnilist,
        "jikan": FetchJikan,
    }
    cls = source_map.get(data_source)
    if cls is None:
        raise InvalidDataSource(
            f"Invalid data source provided ({data_source}), expected ({VALID_DATA_SOURCES})"
        )
    return cls()
