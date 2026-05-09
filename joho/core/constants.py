from typing import Literal, get_args

DATA_SOURCES = Literal["anilist", "jikan"]
VALID_DATA_SOURCES = get_args(DATA_SOURCES)

DEFAULT_ENTRY_INDEX = 0

# key: passed down from main until normalizer
# value: received by fetcher (MAP.get(key))
FETCH_SORT_MAP = {
    "rating": "SCORE_DESC",
    "popularity": "POPULARITY_DESC",
    "trending": "TRENDING_DESC",
    "relevance": "SEARCH_MATCH",
    "newest": "START_DATE_DESC",
    "oldest": "START_DATE",
}
