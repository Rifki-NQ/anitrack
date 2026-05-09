from typing import Literal, get_args

DATA_SOURCES = Literal["anilist", "jikan"]
VALID_DATA_SOURCES = get_args(DATA_SOURCES)

DEFAULT_ENTRY_INDEX = 0

# key: passed down from main until normalizer
# value: received by fetcher (MAP.get(key))
FETCH_SORT_MAP = {
    "rating": "SCORE",
    "popularity": "POPULARITY",
    "trending": "TRENDING",
    "relevance": "SEARCH_MATCH",
    "newest": "START_DATE",
    "oldest": "START_DATE_DESC",
}
