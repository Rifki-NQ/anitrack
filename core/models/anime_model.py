from dataclasses import dataclass
from typing import Literal, get_args

DATA_SOURCES = Literal["anilist", "jikan"]
VALID_DATA_SOURCES = get_args(DATA_SOURCES)

@dataclass
class AnimeDataModel:
    source: DATA_SOURCES
    id: int
    english_title: str | None
    romaji_title: str
    average_score: int | float | None
    episodes: int | None
    genres: list[str]