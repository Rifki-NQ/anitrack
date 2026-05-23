import pytest
import argparse
from joho.main import build_parser
from joho.core.cli.fetch_cli import FetchCLI
from joho.core.normalizers.normalizer_factory import create_normalizer
from joho.core.models.protocols import NormalizerProtocol
from tests.mock_classes.mock_jikan_fetcher import (
    MockJikanFetcherNormal,
    MockJikanFetcherAnimeNotFoundError,
)


@pytest.fixture
def parser() -> argparse.ArgumentParser:
    return build_parser()


@pytest.fixture
def fetch_cli() -> FetchCLI:
    return FetchCLI()


@pytest.fixture
def single_normalizer() -> list[NormalizerProtocol]:
    return [create_normalizer("jikan", MockJikanFetcherNormal())]


@pytest.fixture
def fetch_single_by_title(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(
        ["fetch", "--source", "jikan", "--title", "attack on titan"]
    )


@pytest.fixture
def fetch_single_by_id(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(["fetch", "--source", "jikan", "--id", "16498"])


@pytest.fixture
def fetch_single_flag_entry(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(
        [
            "fetch",
            "--source",
            "jikan",
            "--title",
            "attack on titan",
            "--entry",
            "2",
        ]
    )


@pytest.fixture
def fetch_single_show_title(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(
        [
            "fetch",
            "--source",
            "jikan",
            "--title",
            "attack on titan",
            "--show-title",
        ]
    )


@pytest.fixture
def fetch_single_show_title_max_entry(
    parser: argparse.ArgumentParser,
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "fetch",
            "--source",
            "jikan",
            "--title",
            "attack on titan",
            "--show-title",
            "--max-entry",
            "2",
        ]
    )


@pytest.fixture
def fetch_single_flag_entry_out_of_bound(
    parser: argparse.ArgumentParser,
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "fetch",
            "--source",
            "jikan",
            "--title",
            "attack on titan",
            "--entry",
            "10",
        ]
    )


# uses jikan mocked data
async def test_fetch_single_by_title(
    capsys: pytest.CaptureFixture[str],
    fetch_single_by_title: argparse.Namespace,
    fetch_cli: FetchCLI,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    await fetch_cli.handle_fetch_cli(fetch_single_by_title, False, single_normalizer)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """data_source: jikan
id: 16498
romaji_title: Shingeki no Kyojin
english_title: Attack on Titan
format: TV
episodes: 25
status: Finished Airing
average_score: 8.57
duration: 00:24
start_date: 2013-04-07
end_date: 2013-09-29
studio: Wit Studio
source: Manga
genres: Action|Award Winning|Drama|Suspense
all_time_rank: 125
all_time_popularity: 1

"""
    )


# uses jikan mocked data
async def test_fetch_single_by_id(
    capsys: pytest.CaptureFixture[str],
    fetch_single_by_id: argparse.Namespace,
    fetch_cli: FetchCLI,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    await fetch_cli.handle_fetch_cli(fetch_single_by_id, False, single_normalizer)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """data_source: jikan
id: 16498
romaji_title: Shingeki no Kyojin
english_title: Attack on Titan
format: TV
episodes: 25
status: Finished Airing
average_score: 8.57
duration: 00:24
start_date: 2013-04-07
end_date: 2013-09-29
studio: Wit Studio
source: Manga
genres: Action|Award Winning|Drama|Suspense
all_time_rank: 125
all_time_popularity: 1

"""
    )


# uses jikan mocked data
async def test_fetch_single_flag_entry(
    capsys: pytest.CaptureFixture[str],
    fetch_single_flag_entry: argparse.Namespace,
    fetch_cli: FetchCLI,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    await fetch_cli.handle_fetch_cli(fetch_single_flag_entry, False, single_normalizer)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """data_source: jikan
id: 59571
romaji_title: Shingeki no Kyojin Movie: Kanketsu-hen - The Last Attack
english_title: Attack on Titan: The Last Attack
format: Movie
episodes: 1
status: Finished Airing
average_score: 8.83
duration: 02:24
start_date: 2024-11-08
end_date: None
studio: MAPPA
source: Manga
genres: Action|Drama|Suspense
all_time_rank: 32
all_time_popularity: 2639

"""
    )


# uses jikan mocked data
async def test_fetch_single_show_title(
    capsys: pytest.CaptureFixture[str],
    fetch_single_show_title: argparse.Namespace,
    fetch_cli: FetchCLI,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    await fetch_cli.handle_fetch_cli(fetch_single_show_title, False, single_normalizer)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """Source: jikan
Romaji title | English title
0. Shingeki no Kyojin | Attack on Titan
1. Shingeki no Kyotou | Attack on Skytree
2. Shingeki no Kyojin Movie: Kanketsu-hen - The Last Attack | Attack on Titan: The Last Attack

"""
    )


# uses jikan mocked data
async def test_fetch_single_show_title_max_entry(
    capsys: pytest.CaptureFixture[str],
    fetch_single_show_title_max_entry: argparse.Namespace,
    fetch_cli: FetchCLI,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    await fetch_cli.handle_fetch_cli(
        fetch_single_show_title_max_entry, False, single_normalizer
    )
    captured = capsys.readouterr()
    assert (
        captured.out
        == """Source: jikan
Romaji title | English title
0. Shingeki no Kyojin | Attack on Titan
1. Shingeki no Kyotou | Attack on Skytree

"""
    )


# uses jikan with AnimeNotFoundError raised
async def test_fetch_single_anime_not_found_by_title(
    capsys: pytest.CaptureFixture[str],
    fetch_single_by_title: argparse.Namespace,
    fetch_cli: FetchCLI,
) -> None:
    with pytest.raises(SystemExit) as exit_info:
        await fetch_cli.handle_fetch_cli(
            fetch_single_by_title,
            False,
            [create_normalizer("jikan", MockJikanFetcherAnimeNotFoundError())],
        )
    assert exit_info.value.code == 1
    captured = capsys.readouterr()
    assert (
        captured.err
        == "data_source: jikan\nError: searched anime (attack on titan) not found\n"
    )


# uses jikan mocked data
async def test_fetch_single_out_of_bound_index(
    capsys: pytest.CaptureFixture[str],
    fetch_single_flag_entry_out_of_bound: argparse.Namespace,
    fetch_cli: FetchCLI,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    with pytest.raises(SystemExit) as exit_info:
        await fetch_cli.handle_fetch_cli(
            fetch_single_flag_entry_out_of_bound, False, single_normalizer
        )
    assert exit_info.value.code == 1
    captured = capsys.readouterr()
    assert (
        captured.err
        == "data_source: jikan\nError: out of bound entry index: 10, for title: attack on titan\n"
    )
