from typing import Literal, get_args

DATA_SOURCES = Literal["anilist", "jikan"]
VALID_DATA_SOURCES = get_args(DATA_SOURCES)

# default values are passed inside helper functions in cli_utils.py
DEFAULT_ENTRY_INDEX = 0
DEFAULT_SORT_CHOICE = "relevance"

SORT_CHOICES = ("rating", "popularity", "relevance", "newest", "oldest")

GLOBAL_TIMEOUT = 3.0
