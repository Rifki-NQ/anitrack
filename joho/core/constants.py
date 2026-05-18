from typing import Literal, get_args

DATA_SOURCES = Literal["anilist", "jikan"]
VALID_DATA_SOURCES = get_args(DATA_SOURCES)

DEFAULT_ENTRY_INDEX = 0

SORT_CHOICES = ("rating", "popularity", "relevance", "newest", "oldest")
# default sort is passed inside helper: resolve_sort() in cli_utils
DEFAULT_SORT_CHOICE = "relevance"

GLOBAL_TIMEOUT = 3.0
