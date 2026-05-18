import pytest
import argparse
from joho.main import build_parser
from joho.core.cli.fetch_cli import FetchCLI
from joho.core.normalizers.normalizer_factory import create_normalizer
from joho.core.models.protocols import NormalizerProtocol
from tests.mock_classes.mock_anilist_fetcher import MockAnilistFetcherNormal
from tests.mock_classes.mock_jikan_fetcher import MockJikanFetcherNormal


@pytest.fixture
def parser() -> argparse.ArgumentParser:
    return build_parser()


@pytest.fixture
def fetch_single_by_title(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(
        ["fetch", "--source", "jikan", "--title", "attack on titan"]
    )


@pytest.fixture
def fetch_multi_by_title(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(["fetch", "--source", "all", "--title", "attack on titan"])


@pytest.fixture
def fetch_single_by_id(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(["fetch", "--source", "jikan", "--id", "16498"])


@pytest.fixture
def fetch_multi_by_id(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(["fetch", "--source", "all", "--id", "16498"])


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
def fetch_multi_show_title(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(
        [
            "fetch",
            "--source",
            "all",
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
def fetch_multi_show_title_max_entry(
    parser: argparse.ArgumentParser,
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "fetch",
            "--source",
            "all",
            "--title",
            "attack on titan",
            "--show-title",
            "--max-entry",
            "2",
        ]
    )


@pytest.fixture
def fetch_cli() -> FetchCLI:
    return FetchCLI()


@pytest.fixture
def single_normalizer() -> list[NormalizerProtocol]:
    return [create_normalizer("jikan", MockJikanFetcherNormal())]


@pytest.fixture
def multiple_normalizers() -> list[NormalizerProtocol]:
    return [
        create_normalizer("anilist", MockAnilistFetcherNormal()),
        create_normalizer("jikan", MockJikanFetcherNormal()),
    ]


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


# uses anilist and jikan mocked data
async def test_fetch_multi_by_title(
    capsys: pytest.CaptureFixture[str],
    fetch_multi_by_title: argparse.Namespace,
    fetch_cli: FetchCLI,
    multiple_normalizers: list[NormalizerProtocol],
) -> None:
    await fetch_cli.handle_fetch_cli(fetch_multi_by_title, True, multiple_normalizers)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """data_source: anilist
id: 16498
romaji_title: Shingeki no Kyojin
english_title: Attack on Titan
format: TV
episodes: 25
status: FINISHED
average_score: 85.0
duration: 00:24
start_date: 2013-04-07
end_date: 2013-09-28
studio: WIT STUDIO
source: MANGA
genres: Action|Drama|Fantasy|Mystery
all_time_rank: 67
all_time_popularity: 1

data_source: jikan
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

2 / 2 fetched successfully
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


# uses anilist and jikan mocked data
async def test_fetch_multi_by_id(
    capsys: pytest.CaptureFixture[str],
    fetch_multi_by_id: argparse.Namespace,
    fetch_cli: FetchCLI,
    multiple_normalizers: list[NormalizerProtocol],
) -> None:
    await fetch_cli.handle_fetch_cli(fetch_multi_by_id, True, multiple_normalizers)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """data_source: anilist
id: 16498
romaji_title: Shingeki no Kyojin
english_title: Attack on Titan
format: TV
episodes: 25
status: FINISHED
average_score: 85.0
duration: 00:24
start_date: 2013-04-07
end_date: 2013-09-28
studio: WIT STUDIO
source: MANGA
genres: Action|Drama|Fantasy|Mystery
all_time_rank: 67
all_time_popularity: 1

data_source: jikan
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

2 / 2 fetched successfully
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


# uses anilist and jikan mocked data
async def test_fetch_multi_show_title(
    capsys: pytest.CaptureFixture[str],
    fetch_multi_show_title: argparse.Namespace,
    fetch_cli: FetchCLI,
    multiple_normalizers: list[NormalizerProtocol],
) -> None:
    await fetch_cli.handle_fetch_cli(fetch_multi_show_title, True, multiple_normalizers)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """Source: anilist
Romaji title | English title
0. Shingeki no Kyojin | Attack on Titan
1. Shingeki no Kyojin: The Final Season | Attack on Titan Final Season
2. Shingeki no Kyojin OVA | Attack on Titan OVA
3. Shingeki no Kyojin Season 2 | Attack on Titan Season 2
4. Shingeki no Kyojin Season 3 | Attack on Titan Season 3
5. Shingeki no Kyojin Gaiden: Kuinaki Sentaku | Attack on Titan: No Regrets
6. Shingeki no Kyojin: Chronicle | Attack on Titan ~Chronicle~
7. Shingeki no Kyojin: Chimi Kyara Gekijou - Tondeke! Kunren Heidan | Attack on Titan Picture Drama
8. Shingeki no Kyojin: LOST GIRLS | Attack on Titan: Lost Girls
9. Shingeki! Kyojin Chuugakkou | Attack on Titan: Junior High
10. Shingeki no Kyojin Season 2: Kakusei no Houkou | Attack on Titan: The Roar of Awakening
11. Shingeki no Kyojin: Chimi Kyara Gekijou - Final | Attack On Titan: The Final Season Specials
12. Shingeki no Kyojin: The Final Season Part 2 | Attack on Titan Final Season Part 2
13. Shingeki no Kyojin Kouhen: Jiyuu no Tsubasa | Attack on Titan Part II: Wings of Freedom
14. Shingeki no Kyojin Season 3 Part 2 | Attack on Titan Season 3 Part 2
15. Shingeki no Kyojin: Chimi Kyara Gekijou - Rivai-han | None
16. Shingeki no Kyojin: The Final Season - Kanketsu-hen Kouhen | Attack on Titan Final Season THE FINAL CHAPTERS Special 2
17. Shingeki no Kyojin: Chimi Kyara Gekijou - Rivai-han Part 2 | None
18. Shingeki no Kyojin: The Final Season - Kanketsu-hen Zenpen | Attack on Titan Final Season THE FINAL CHAPTERS Special 1
19. Shingeki no Kyojin Zenpen: Guren no Yumiya | Attack on Titan Part I: Crimson Bow and Arrow

Source: jikan
Romaji title | English title
0. Shingeki no Kyojin | Attack on Titan
1. Shingeki no Kyotou | Attack on Skytree
2. Shingeki no Kyojin Movie: Kanketsu-hen - The Last Attack | Attack on Titan: The Last Attack

2 / 2 fetched successfully
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


# uses anilist and jikan mocked data
async def test_fetch_multi_show_title_max_entry(
    capsys: pytest.CaptureFixture[str],
    fetch_multi_show_title_max_entry: argparse.Namespace,
    fetch_cli: FetchCLI,
    multiple_normalizers: list[NormalizerProtocol],
) -> None:
    await fetch_cli.handle_fetch_cli(
        fetch_multi_show_title_max_entry, True, multiple_normalizers
    )
    captured = capsys.readouterr()
    assert (
        captured.out
        == """Source: anilist
Romaji title | English title
0. Shingeki no Kyojin | Attack on Titan
1. Shingeki no Kyojin: The Final Season | Attack on Titan Final Season

Source: jikan
Romaji title | English title
0. Shingeki no Kyojin | Attack on Titan
1. Shingeki no Kyotou | Attack on Skytree

2 / 2 fetched successfully
"""
    )
