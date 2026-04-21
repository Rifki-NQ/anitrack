import pytest
from tests.fetchers_mock_data import MockAnilistFetcher, MockJikanFetcher
from core.normalizers.normalizer_factory import create_normalizer
from core.models.anime_model import AnimeDataModel
from core.models.protocols import NormalizerProtocol

@pytest.fixture
def anilist_normalizer() -> NormalizerProtocol:
    return create_normalizer("anilist", MockAnilistFetcher())

@pytest.fixture
def jikan_normalizer() -> NormalizerProtocol:
    return create_normalizer("jikan", MockJikanFetcher())

@pytest.fixture
def anime_data_model_anilist(anilist_normalizer: NormalizerProtocol) -> AnimeDataModel:
    return anilist_normalizer.get_anime_by_title("Attack on titan")

@pytest.fixture
def anime_data_model_jikan(jikan_normalizer: NormalizerProtocol) -> AnimeDataModel:
    return jikan_normalizer.get_anime_by_title("Attack on titan")

def test_response_normalizer_anilist_value(anime_data_model_anilist: AnimeDataModel):
    assert anime_data_model_anilist.id == 16498
    assert anime_data_model_anilist.source == "anilist"
    assert anime_data_model_anilist.english_title == "Attack on Titan"
    assert anime_data_model_anilist.romaji_title == "Shingeki no Kyojin"
    assert anime_data_model_anilist.average_score == 85
    assert anime_data_model_anilist.episodes == 25
    assert anime_data_model_anilist.genres == ['Action', 'Drama', 'Fantasy', 'Mystery']

def test_response_normalizer_jikan_value(anime_data_model_jikan: AnimeDataModel):
    assert anime_data_model_jikan.id == 16498
    assert anime_data_model_jikan.source == "jikan"
    assert anime_data_model_jikan.english_title == "Attack on Titan"
    assert anime_data_model_jikan.romaji_title == "Shingeki no Kyojin"
    assert anime_data_model_jikan.average_score == 8.57
    assert anime_data_model_jikan.episodes == 25
    assert anime_data_model_jikan.genres == ['Action', 'Award Winning', 'Drama', 'Suspense']