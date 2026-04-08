import pytest
from tests.fetchers_mock_data import MockAnilistFetcher, MockJikanFetcher
from core.normalizer import ResponseNormalizer
from core.models.anime_model import AnimeDataModel

@pytest.fixture
def response_normalizer() -> ResponseNormalizer:
    return ResponseNormalizer(MockAnilistFetcher(), MockJikanFetcher())

@pytest.fixture
def anime_data_model_anilist(response_normalizer: ResponseNormalizer) -> AnimeDataModel:
    return response_normalizer.get_anime_data_by_title("anilist", "Attack on titan", 0)

@pytest.fixture
def anime_data_model_jikan(response_normalizer: ResponseNormalizer) -> AnimeDataModel:
    return response_normalizer.get_anime_data_by_title("jikan", "Attack on titan", 0)

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