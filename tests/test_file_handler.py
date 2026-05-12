import pytest
import pytest_asyncio
from pathlib import Path
from dataclasses import fields
from tests.fetchers_mock_data import MockAnilistFetcher
from joho.core.normalizers.normalizer_factory import create_normalizer
from joho.core.file_handler import DataIO
from joho.core.models.protocols import NormalizerProtocol
from joho.core.models.anime_model import AnimeDataModel


@pytest.fixture
def anilist_normalizer() -> NormalizerProtocol:
    return create_normalizer("anilist", MockAnilistFetcher())


@pytest_asyncio.fixture
async def anilist_anime_data_model(
    anilist_normalizer: NormalizerProtocol,
) -> list[AnimeDataModel]:
    return await anilist_normalizer.get_all_anime_by_title(
        "Attack on titan", "relevance"
    )


@pytest.fixture
def data(
    anilist_anime_data_model: list[AnimeDataModel], tmp_path: Path
) -> list[dict[str, str | None]]:
    filepath = tmp_path / "anime_data.csv"
    file_handler = DataIO(filepath)
    # save all entries to file
    for data in anilist_anime_data_model:
        file_handler.save_data(data, overwrite=False)
    assert filepath.exists()
    assert filepath.stat().st_size > 0
    return file_handler.read_data()


def test_data_length(
    data: list[dict[str, str | None]], anilist_anime_data_model: list[AnimeDataModel]
) -> None:
    # before save to the file
    assert len(anilist_anime_data_model) == 20
    # after save, then read from the file
    assert len(data) == 20


# entry with no None \ empty value
@pytest.fixture
def first_data(data: list[dict[str, str | None]]) -> dict[str, str | None]:
    return data[0]


# entry with 'english_title' and 'rankings' as None \ empty value
@pytest.fixture
def seventeenth_data(data: list[dict[str, str | None]]) -> dict[str, str | None]:
    return data[17]


def test_first_data_headers(first_data: dict[str, str | None]) -> None:
    headers = [f.name for f in fields(AnimeDataModel)]
    for key in first_data.keys():
        assert key in headers


def test_first_data_values(first_data: dict[str, str | None]) -> None:
    assert first_data["data_source"] == "anilist"
    assert first_data["id"] == "16498"
    assert first_data["romaji_title"] == "Shingeki no Kyojin"
    assert first_data["english_title"] == "Attack on Titan"
    assert first_data["format"] == "TV"
    assert first_data["episodes"] == "25"
    assert first_data["status"] == "FINISHED"
    assert first_data["average_score"] == "85.0"
    assert first_data["duration"] == "00:24"
    assert first_data["start_date"] == "2013-04-07"
    assert first_data["end_date"] == "2013-09-28"
    assert first_data["studio"] == "WIT STUDIO"
    assert first_data["source"] == "MANGA"
    assert first_data["genres"] == "Action|Drama|Fantasy|Mystery"
    assert first_data["all_time_rank"] == "73"
    assert first_data["all_time_popularity"] == "1"


def test_seventeenth_data_values(seventeenth_data: dict[str, str | None]) -> None:
    assert seventeenth_data["data_source"] == "anilist"
    assert seventeenth_data["id"] == "108942"
    assert (
        seventeenth_data["romaji_title"]
        == "Shingeki no Kyojin: Chimi Kyara Gekijou - Rivai-han"
    )
    assert seventeenth_data["english_title"] is None
    assert seventeenth_data["format"] == "SPECIAL"
    assert seventeenth_data["episodes"] == "4"
    assert seventeenth_data["status"] == "FINISHED"
    assert seventeenth_data["average_score"] == "75.0"
    assert seventeenth_data["duration"] == "00:02"
    assert seventeenth_data["start_date"] == "2018-10-17"
    assert seventeenth_data["end_date"] == "2019-02-27"
    assert seventeenth_data["studio"] == "WIT STUDIO"
    assert seventeenth_data["source"] == "MANGA"
    assert seventeenth_data["genres"] == "Comedy|Fantasy"
    assert seventeenth_data["all_time_rank"] is None
    assert seventeenth_data["all_time_popularity"] is None
