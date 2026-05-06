import pytest
from pathlib import Path
from tests.fetchers_mock_data import MockAnilistFetcher
from joho.core.normalizers.normalizer_factory import create_normalizer
from joho.core.file_handler import DataIO
from joho.core.models.protocols import NormalizerProtocol
from joho.core.models.anime_model import AnimeDataModel


@pytest.fixture
def anilist_normalizer() -> NormalizerProtocol:
    return create_normalizer("anilist", MockAnilistFetcher())


@pytest.fixture
def anilist_anime_data_model(anilist_normalizer: NormalizerProtocol) -> AnimeDataModel:
    return anilist_normalizer.get_anime_by_title("Attack on titan")

@pytest.fixture
def save_data(anilist_anime_data_model: AnimeDataModel, tmp_path: Path) -> list[dict[str, str | None]]:
    filepath = tmp_path / "anime_data.csv"
    file_handler = DataIO(filepath)
    file_handler.save_data(anilist_anime_data_model, overwrite=False)
    assert filepath.exists()
    return file_handler.read_data()