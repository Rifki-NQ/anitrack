from dataclasses import dataclass
from core.constants import DATA_SOURCES

@dataclass
class AnimeDataModel:
    data_source: DATA_SOURCES
    id: int
    romaji_title: str
    english_title: str | None
    format: str | None
    episodes: int | None
    status: str | None
    average_score: int | float | None
    duration: int | None
    start_date: str | None
    end_date: str | None
    studio: str | None
    source: str | None
    genres: list[str]
    all_time_rank: int | None
    all_time_popularity: int | None