import pytest
import argparse
from pathlib import Path
from joho.main import build_parser
from joho.core.cli.read_cli import ReadCLI
from joho.core.file_handler import DataIO

# by default, read --limit is 10 when not provided


@pytest.fixture
def parser() -> argparse.ArgumentParser:
    return build_parser()


@pytest.fixture
def mock_data_path() -> Path:
    return Path("tests") / "mock_data" / "steins_gate.csv"


@pytest.fixture
def read(parser: argparse.ArgumentParser, mock_data_path: Path) -> argparse.Namespace:
    return parser.parse_args(["read", "--path", str(mock_data_path)])


@pytest.fixture
def read_with_limit(
    parser: argparse.ArgumentParser, mock_data_path: Path
) -> argparse.Namespace:
    return parser.parse_args(["read", "--path", str(mock_data_path), "--limit", "2"])


@pytest.fixture
def read_with_limit_0(
    parser: argparse.ArgumentParser, mock_data_path: Path
) -> argparse.Namespace:
    return parser.parse_args(["read", "--path", str(mock_data_path), "--limit", "0"])


@pytest.fixture
def read_entry(
    parser: argparse.ArgumentParser, mock_data_path: Path
) -> argparse.Namespace:
    return parser.parse_args(["read", "--path", str(mock_data_path), "--entry", "4"])


@pytest.fixture
def read_show_title(
    parser: argparse.ArgumentParser, mock_data_path: Path
) -> argparse.Namespace:
    return parser.parse_args(["read", "--path", str(mock_data_path), "--show-title"])


@pytest.fixture
def read_show_title_with_limit(
    parser: argparse.ArgumentParser, mock_data_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        ["read", "--path", str(mock_data_path), "--show-title", "--limit", "2"]
    )


@pytest.fixture
def read_show_title_with_limit_0(
    parser: argparse.ArgumentParser, mock_data_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        ["read", "--path", str(mock_data_path), "--show-title", "--limit", "0"]
    )


def test_read(read: argparse.Namespace, capsys: pytest.CaptureFixture[str]) -> None:
    read_cli = ReadCLI(DataIO(read.path))
    read_cli.handle_read_cli(read)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """data_source: anilist
id: 9253
romaji_title: Steins;Gate
english_title: Steins;Gate
format: TV
episodes: 24
status: FINISHED
average_score: 89.0
duration: 00:24
start_date: 2011-04-06
end_date: 2011-09-14
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Drama|Psychological|Sci-Fi|Thriller
all_time_rank: 8
all_time_popularity: 27

data_source: anilist
id: 21127
romaji_title: Steins;Gate 0
english_title: Steins;Gate 0
format: TV
episodes: 23
status: FINISHED
average_score: 84.0
duration: 00:24
start_date: 2018-04-12
end_date: 2018-09-27
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Drama|Psychological|Sci-Fi|Thriller
all_time_rank: 101
all_time_popularity: 225

data_source: anilist
id: 104174
romaji_title: Steins;Gate 0: Kesshou Takei no Valentine - Bittersweet Day
english_title: Steins;Gate 0: Valentine's of Crystal Polymorphism -Bittersweet Intermedio-
format: OVA
episodes: 1
status: FINISHED
average_score: 71.0
duration: 00:24
start_date: 2018-12-21
end_date: 2018-12-21
studio: WHITE FOX
source: ORIGINAL
genres: Comedy|Sci-Fi
all_time_rank: None
all_time_popularity: 91

data_source: anilist
id: 10863
romaji_title: Steins;Gate: Oukoubakko no Poriomania
english_title: Steins;Gate: Egoistic Poriomania
format: OVA
episodes: 1
status: FINISHED
average_score: 81.0
duration: 00:25
start_date: 2012-02-22
end_date: 2012-02-22
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Comedy|Romance|Sci-Fi
all_time_rank: 16
all_time_popularity: 7

data_source: anilist
id: 21624
romaji_title: Steins;Gate: Kyoukaimenjou no Missing Link - Divide By Zero
english_title: Steins;Gate 0: 23β -Divide by Zero-
format: OVA
episodes: 1
status: FINISHED
average_score: 81.0
duration: 00:24
start_date: 2015-12-03
end_date: 2015-12-03
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Drama|Psychological|Sci-Fi|Thriller
all_time_rank: 12
all_time_popularity: 21

data_source: anilist
id: 20907
romaji_title: Steins;Gate: Soumei Eichi no Cognitive Computing
english_title: None
format: ONA
episodes: 4
status: FINISHED
average_score: 72.0
duration: 00:04
start_date: 2014-10-14
end_date: 2014-11-11
studio: WHITE FOX
source: ORIGINAL
genres: Comedy|Sci-Fi
all_time_rank: None
all_time_popularity: None

data_source: anilist
id: 11577
romaji_title: Steins;Gate: Fuka Ryouiki no Déjà vu
english_title: Steins;Gate The Movie – Load Region of Déjà Vu
format: MOVIE
episodes: 1
status: FINISHED
average_score: 82.0
duration: 01:30
start_date: 2013-04-20
end_date: 2013-04-20
studio: WHITE FOX
source: ORIGINAL
genres: Drama|Romance|Sci-Fi|Thriller
all_time_rank: 60
all_time_popularity: 46

data_source: jikan
id: 9253
romaji_title: Steins;Gate
english_title: Steins;Gate
format: TV
episodes: 24
status: Finished Airing
average_score: 9.07
duration: 00:24
start_date: 2011-04-06
end_date: 2011-09-14
studio: White Fox
source: Visual novel
genres: Drama|Sci-Fi|Suspense
all_time_rank: 5
all_time_popularity: 14

data_source: jikan
id: 27957
romaji_title: Steins;Gate: Soumei Eichi no Cognitive Computing
english_title: Steins;Gate: The Sagacious Wisdom of Cognitive Computing
format: ONA
episodes: 4
status: Finished Airing
average_score: 7.44
duration: 00:03
start_date: 2014-10-15
end_date: 2014-11-12
studio: White Fox
source: Visual novel
genres: Comedy|Sci-Fi
all_time_rank: 2578
all_time_popularity: 2123

data_source: jikan
id: 32188
romaji_title: Steins;Gate: Kyoukaimenjou no Missing Link - Divide By Zero
english_title: Steins;Gate: Open the Missing Link - Divide By Zero
format: TV Special
episodes: 1
status: Finished Airing
average_score: 8.27
duration: 00:24
start_date: 2015-12-03
end_date: None
studio: White Fox
source: Visual novel
genres: Sci-Fi|Suspense
all_time_rank: 361
all_time_popularity: 971

"""
    )


def test_read_with_limit(
    read_with_limit: argparse.Namespace, capsys: pytest.CaptureFixture[str]
) -> None:
    read_cli = ReadCLI(DataIO(read_with_limit.path))
    read_cli.handle_read_cli(read_with_limit)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """data_source: anilist
id: 9253
romaji_title: Steins;Gate
english_title: Steins;Gate
format: TV
episodes: 24
status: FINISHED
average_score: 89.0
duration: 00:24
start_date: 2011-04-06
end_date: 2011-09-14
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Drama|Psychological|Sci-Fi|Thriller
all_time_rank: 8
all_time_popularity: 27

data_source: anilist
id: 21127
romaji_title: Steins;Gate 0
english_title: Steins;Gate 0
format: TV
episodes: 23
status: FINISHED
average_score: 84.0
duration: 00:24
start_date: 2018-04-12
end_date: 2018-09-27
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Drama|Psychological|Sci-Fi|Thriller
all_time_rank: 101
all_time_popularity: 225

"""
    )


def test_read_entry(
    read_entry: argparse.Namespace, capsys: pytest.CaptureFixture[str]
) -> None:
    read_cli = ReadCLI(DataIO(read_entry.path))
    read_cli.handle_read_cli(read_entry)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """data_source: anilist
id: 21624
romaji_title: Steins;Gate: Kyoukaimenjou no Missing Link - Divide By Zero
english_title: Steins;Gate 0: 23β -Divide by Zero-
format: OVA
episodes: 1
status: FINISHED
average_score: 81.0
duration: 00:24
start_date: 2015-12-03
end_date: 2015-12-03
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Drama|Psychological|Sci-Fi|Thriller
all_time_rank: 12
all_time_popularity: 21
"""
    )


def test_read_show_title(
    read_show_title: argparse.Namespace, capsys: pytest.CaptureFixture[str]
) -> None:
    read_cli = ReadCLI(DataIO(read_show_title.path))
    read_cli.handle_read_cli(read_show_title)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """Entry_num | Data source | Romaji title | English title
0. anilist | Steins;Gate | Steins;Gate
1. anilist | Steins;Gate 0 | Steins;Gate 0
2. anilist | Steins;Gate 0: Kesshou Takei no Valentine - Bittersweet Day | Steins;Gate 0: Valentine's of Crystal Polymorphism -Bittersweet Intermedio-
3. anilist | Steins;Gate: Oukoubakko no Poriomania | Steins;Gate: Egoistic Poriomania
4. anilist | Steins;Gate: Kyoukaimenjou no Missing Link - Divide By Zero | Steins;Gate 0: 23β -Divide by Zero-
5. anilist | Steins;Gate: Soumei Eichi no Cognitive Computing | None
6. anilist | Steins;Gate: Fuka Ryouiki no Déjà vu | Steins;Gate The Movie – Load Region of Déjà Vu
7. jikan | Steins;Gate | Steins;Gate
8. jikan | Steins;Gate: Soumei Eichi no Cognitive Computing | Steins;Gate: The Sagacious Wisdom of Cognitive Computing
9. jikan | Steins;Gate: Kyoukaimenjou no Missing Link - Divide By Zero | Steins;Gate: Open the Missing Link - Divide By Zero
"""
    )


def test_read_show_title_with_limit(
    read_show_title_with_limit: argparse.Namespace, capsys: pytest.CaptureFixture[str]
) -> None:
    read_cli = ReadCLI(DataIO(read_show_title_with_limit.path))
    read_cli.handle_read_cli(read_show_title_with_limit)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """Entry_num | Data source | Romaji title | English title
0. anilist | Steins;Gate | Steins;Gate
1. anilist | Steins;Gate 0 | Steins;Gate 0
"""
    )


def test_read_show_title_limit_0(
    read_show_title_with_limit_0: argparse.Namespace, capsys: pytest.CaptureFixture[str]
) -> None:
    read_cli = ReadCLI(DataIO(read_show_title_with_limit_0.path))
    read_cli.handle_read_cli(read_show_title_with_limit_0)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """Entry_num | Data source | Romaji title | English title
0. anilist | Steins;Gate | Steins;Gate
1. anilist | Steins;Gate 0 | Steins;Gate 0
2. anilist | Steins;Gate 0: Kesshou Takei no Valentine - Bittersweet Day | Steins;Gate 0: Valentine's of Crystal Polymorphism -Bittersweet Intermedio-
3. anilist | Steins;Gate: Oukoubakko no Poriomania | Steins;Gate: Egoistic Poriomania
4. anilist | Steins;Gate: Kyoukaimenjou no Missing Link - Divide By Zero | Steins;Gate 0: 23β -Divide by Zero-
5. anilist | Steins;Gate: Soumei Eichi no Cognitive Computing | None
6. anilist | Steins;Gate: Fuka Ryouiki no Déjà vu | Steins;Gate The Movie – Load Region of Déjà Vu
7. jikan | Steins;Gate | Steins;Gate
8. jikan | Steins;Gate: Soumei Eichi no Cognitive Computing | Steins;Gate: The Sagacious Wisdom of Cognitive Computing
9. jikan | Steins;Gate: Kyoukaimenjou no Missing Link - Divide By Zero | Steins;Gate: Open the Missing Link - Divide By Zero
10. jikan | Steins;Gate: Oukoubakko no Poriomania | Steins;Gate: Egoistic Poriomania
11. jikan | Steins;Gate Movie: Fuka Ryouiki no Déjà vu | Steins;Gate: The Movie - Load Region of Déjà Vu
12. jikan | Steins;Gate 0: Kesshou Takei no Valentine - Bittersweet Intermedio | Steins;Gate 0: Valentine's of Crystal Polymorphism -Bittersweet Intermedio-
13. jikan | Steins;Gate 0 | Steins;Gate 0
14. jikan | Gate: Jieitai Kanochi nite, Kaku Tatakaeri | GATE
15. jikan | Kara no Kyoukai Remix: Gate of Seventh Heaven | The Garden of Sinners Remix: Gate of Seventh Heaven
16. jikan | Gate: Jieitai Kanochi nite, Kaku Tatakaeri Part 2 | GATE Part 2
17. jikan | The New Gate | The New Gate
18. jikan | Gate Season 2: Jieitai Kanoumi nite, Kaku Tatakaeri | Gate 2: Tides of Conflict
19. jikan | Rio: Rainbow Gate! | Rio - Rainbow Gate!: Reshuffle
20. jikan | Cardfight!! Vanguard G: Stride Gate-hen | Cardfight!! Vanguard G Stride Gate
21. jikan | Ikebukuro West Gate Park | Ikebukuro West Gate Park
22. jikan | Divine Gate | Divine Gate
23. jikan | Black Gate: Kanin no Gakuen | None
24. jikan | Rio: Rainbow Gate! Special | None
25. jikan | Gate Keepers 21 | None
26. jikan | Gate Keepers | None
27. jikan | Pokemon Fushigi no Dungeon: Shutsudou Pokemon Kyuujotai Ganbaruzu! | Pokémon Mystery Dungeon: Team Go-Getters Out of the Gate!
28. jikan | Xuan Jie Zhi Men | The Gate of Mystical Realm
29. jikan | Sinbad: Mahiru no Yoru to Fushigi no Mon | Sinbad: Night at High Noon and the Wonder Gate
30. jikan | Luo Xiaohei Zhanji: Zhongsheng Zhi Men | The Legend of Luoxiaohei: The Gate of All Living Beings
31. jikan | Dimension W: W no Tobira Online - Rose no Onayami Soudanshitsu | Dimension W: W Gate Online - Rose's Counseling Room
"""
    )


def test_read_with_limit_0(
    read_with_limit_0: argparse.Namespace, capsys: pytest.CaptureFixture[str]
) -> None:
    read_cli = ReadCLI(DataIO(read_with_limit_0.path))
    read_cli.handle_read_cli(read_with_limit_0)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """data_source: anilist
id: 9253
romaji_title: Steins;Gate
english_title: Steins;Gate
format: TV
episodes: 24
status: FINISHED
average_score: 89.0
duration: 00:24
start_date: 2011-04-06
end_date: 2011-09-14
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Drama|Psychological|Sci-Fi|Thriller
all_time_rank: 8
all_time_popularity: 27

data_source: anilist
id: 21127
romaji_title: Steins;Gate 0
english_title: Steins;Gate 0
format: TV
episodes: 23
status: FINISHED
average_score: 84.0
duration: 00:24
start_date: 2018-04-12
end_date: 2018-09-27
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Drama|Psychological|Sci-Fi|Thriller
all_time_rank: 101
all_time_popularity: 225

data_source: anilist
id: 104174
romaji_title: Steins;Gate 0: Kesshou Takei no Valentine - Bittersweet Day
english_title: Steins;Gate 0: Valentine's of Crystal Polymorphism -Bittersweet Intermedio-
format: OVA
episodes: 1
status: FINISHED
average_score: 71.0
duration: 00:24
start_date: 2018-12-21
end_date: 2018-12-21
studio: WHITE FOX
source: ORIGINAL
genres: Comedy|Sci-Fi
all_time_rank: None
all_time_popularity: 91

data_source: anilist
id: 10863
romaji_title: Steins;Gate: Oukoubakko no Poriomania
english_title: Steins;Gate: Egoistic Poriomania
format: OVA
episodes: 1
status: FINISHED
average_score: 81.0
duration: 00:25
start_date: 2012-02-22
end_date: 2012-02-22
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Comedy|Romance|Sci-Fi
all_time_rank: 16
all_time_popularity: 7

data_source: anilist
id: 21624
romaji_title: Steins;Gate: Kyoukaimenjou no Missing Link - Divide By Zero
english_title: Steins;Gate 0: 23β -Divide by Zero-
format: OVA
episodes: 1
status: FINISHED
average_score: 81.0
duration: 00:24
start_date: 2015-12-03
end_date: 2015-12-03
studio: WHITE FOX
source: VISUAL_NOVEL
genres: Drama|Psychological|Sci-Fi|Thriller
all_time_rank: 12
all_time_popularity: 21

data_source: anilist
id: 20907
romaji_title: Steins;Gate: Soumei Eichi no Cognitive Computing
english_title: None
format: ONA
episodes: 4
status: FINISHED
average_score: 72.0
duration: 00:04
start_date: 2014-10-14
end_date: 2014-11-11
studio: WHITE FOX
source: ORIGINAL
genres: Comedy|Sci-Fi
all_time_rank: None
all_time_popularity: None

data_source: anilist
id: 11577
romaji_title: Steins;Gate: Fuka Ryouiki no Déjà vu
english_title: Steins;Gate The Movie – Load Region of Déjà Vu
format: MOVIE
episodes: 1
status: FINISHED
average_score: 82.0
duration: 01:30
start_date: 2013-04-20
end_date: 2013-04-20
studio: WHITE FOX
source: ORIGINAL
genres: Drama|Romance|Sci-Fi|Thriller
all_time_rank: 60
all_time_popularity: 46

data_source: jikan
id: 9253
romaji_title: Steins;Gate
english_title: Steins;Gate
format: TV
episodes: 24
status: Finished Airing
average_score: 9.07
duration: 00:24
start_date: 2011-04-06
end_date: 2011-09-14
studio: White Fox
source: Visual novel
genres: Drama|Sci-Fi|Suspense
all_time_rank: 5
all_time_popularity: 14

data_source: jikan
id: 27957
romaji_title: Steins;Gate: Soumei Eichi no Cognitive Computing
english_title: Steins;Gate: The Sagacious Wisdom of Cognitive Computing
format: ONA
episodes: 4
status: Finished Airing
average_score: 7.44
duration: 00:03
start_date: 2014-10-15
end_date: 2014-11-12
studio: White Fox
source: Visual novel
genres: Comedy|Sci-Fi
all_time_rank: 2578
all_time_popularity: 2123

data_source: jikan
id: 32188
romaji_title: Steins;Gate: Kyoukaimenjou no Missing Link - Divide By Zero
english_title: Steins;Gate: Open the Missing Link - Divide By Zero
format: TV Special
episodes: 1
status: Finished Airing
average_score: 8.27
duration: 00:24
start_date: 2015-12-03
end_date: None
studio: White Fox
source: Visual novel
genres: Sci-Fi|Suspense
all_time_rank: 361
all_time_popularity: 971

data_source: jikan
id: 10863
romaji_title: Steins;Gate: Oukoubakko no Poriomania
english_title: Steins;Gate: Egoistic Poriomania
format: Special
episodes: 1
status: Finished Airing
average_score: 8.29
duration: 00:24
start_date: 2012-02-22
end_date: None
studio: White Fox
source: Visual novel
genres: Comedy|Sci-Fi
all_time_rank: 339
all_time_popularity: 553

data_source: jikan
id: 11577
romaji_title: Steins;Gate Movie: Fuka Ryouiki no Déjà vu
english_title: Steins;Gate: The Movie - Load Region of Déjà Vu
format: Movie
episodes: 1
status: Finished Airing
average_score: 8.45
duration: 01:30
start_date: 2013-04-20
end_date: None
studio: White Fox
source: Visual novel
genres: Drama|Sci-Fi
all_time_rank: 193
all_time_popularity: 384

data_source: jikan
id: 37492
romaji_title: Steins;Gate 0: Kesshou Takei no Valentine - Bittersweet Intermedio
english_title: Steins;Gate 0: Valentine's of Crystal Polymorphism -Bittersweet Intermedio-
format: Special
episodes: 1
status: Finished Airing
average_score: 7.28
duration: 00:23
start_date: 2018-12-21
end_date: None
studio: White Fox
source: Visual novel
genres: Comedy
all_time_rank: 3485
all_time_popularity: 2103

data_source: jikan
id: 30484
romaji_title: Steins;Gate 0
english_title: Steins;Gate 0
format: TV
episodes: 23
status: Finished Airing
average_score: 8.55
duration: 00:23
start_date: 2018-04-12
end_date: 2018-09-27
studio: White Fox
source: Visual novel
genres: Drama|Sci-Fi|Suspense
all_time_rank: 138
all_time_popularity: 208

data_source: jikan
id: 28907
romaji_title: Gate: Jieitai Kanochi nite, Kaku Tatakaeri
english_title: GATE
format: TV
episodes: 12
status: Finished Airing
average_score: 7.68
duration: 00:23
start_date: 2015-07-04
end_date: 2015-09-19
studio: A-1 Pictures
source: Light novel
genres: Action|Adventure|Fantasy
all_time_rank: 1525
all_time_popularity: 238

data_source: jikan
id: 6624
romaji_title: Kara no Kyoukai Remix: Gate of Seventh Heaven
english_title: The Garden of Sinners Remix: Gate of Seventh Heaven
format: Movie
episodes: 1
status: Finished Airing
average_score: 7.54
duration: 01:01
start_date: 2009-03-14
end_date: None
studio: ufotable
source: Light novel
genres: Action|Fantasy|Mystery|Romance|Suspense
all_time_rank: 2081
all_time_popularity: 3554

data_source: jikan
id: 31637
romaji_title: Gate: Jieitai Kanochi nite, Kaku Tatakaeri Part 2
english_title: GATE Part 2
format: TV
episodes: 12
status: Finished Airing
average_score: 7.71
duration: 00:23
start_date: 2016-01-09
end_date: 2016-03-26
studio: A-1 Pictures
source: Light novel
genres: Action|Adventure|Fantasy
all_time_rank: 1435
all_time_popularity: 413

data_source: jikan
id: 57100
romaji_title: The New Gate
english_title: The New Gate
format: TV
episodes: 12
status: Finished Airing
average_score: 6.47
duration: 00:23
start_date: 2024-04-14
end_date: 2024-06-30
studio: Yokohama Animation Lab
source: Light novel
genres: Action|Adventure|Fantasy
all_time_rank: 8396
all_time_popularity: 1749

data_source: jikan
id: 61973
romaji_title: Gate Season 2: Jieitai Kanoumi nite, Kaku Tatakaeri
english_title: Gate 2: Tides of Conflict
format: TV
episodes: None
status: Not yet aired
average_score: None
duration: None
start_date: 2027-01-01
end_date: None
studio: Studio M2
source: Light novel
genres: Action|Adventure|Fantasy
all_time_rank: None
all_time_popularity: 4412

data_source: jikan
id: 8241
romaji_title: Rio: Rainbow Gate!
english_title: Rio - Rainbow Gate!: Reshuffle
format: TV
episodes: 13
status: Finished Airing
average_score: 5.87
duration: 00:23
start_date: 2011-01-04
end_date: 2011-03-29
studio: Xebec
source: Game
genres: Comedy|Ecchi
all_time_rank: 11674
all_time_popularity: 3852

data_source: jikan
id: 32802
romaji_title: Cardfight!! Vanguard G: Stride Gate-hen
english_title: Cardfight!! Vanguard G Stride Gate
format: TV
episodes: 24
status: Finished Airing
average_score: 6.85
duration: 00:24
start_date: 2016-04-17
end_date: 2016-09-25
studio: TMS Entertainment
source: Card game
genres: Action
all_time_rank: 5999
all_time_popularity: 6796

data_source: jikan
id: 40359
romaji_title: Ikebukuro West Gate Park
english_title: Ikebukuro West Gate Park
format: TV
episodes: 12
status: Finished Airing
average_score: 6.87
duration: 00:23
start_date: 2020-10-06
end_date: 2020-12-22
studio: Doga Kobo
source: Novel
genres: Drama|Mystery
all_time_rank: 5889
all_time_popularity: 2007

data_source: jikan
id: 31710
romaji_title: Divine Gate
english_title: Divine Gate
format: TV
episodes: 12
status: Finished Airing
average_score: 5.53
duration: 00:23
start_date: 2016-01-08
end_date: 2016-03-25
studio: Studio Pierrot
source: Game
genres: Action|Fantasy|Sci-Fi
all_time_rank: 13137
all_time_popularity: 1581

data_source: jikan
id: 2145
romaji_title: Black Gate: Kanin no Gakuen
english_title: None
format: OVA
episodes: 2
status: Finished Airing
average_score: 5.81
duration: 00:28
start_date: 2004-07-25
end_date: 2004-12-25
studio: Studio Jam
source: Visual novel
genres: Fantasy|Hentai
all_time_rank: None
all_time_popularity: 8957

data_source: jikan
id: 10301
romaji_title: Rio: Rainbow Gate! Special
english_title: None
format: Special
episodes: 1
status: Finished Airing
average_score: 6.02
duration: 00:23
start_date: 2011-10-19
end_date: None
studio: Xebec
source: Game
genres: Comedy|Ecchi
all_time_rank: 10940
all_time_popularity: 8831

data_source: jikan
id: 128
romaji_title: Gate Keepers 21
english_title: None
format: OVA
episodes: 6
status: Finished Airing
average_score: 6.79
duration: 00:25
start_date: 2002-04-24
end_date: 2003-01-08
studio: Gonzo
source: Game
genres: Drama|Sci-Fi
all_time_rank: 6384
all_time_popularity: 6856

data_source: jikan
id: 127
romaji_title: Gate Keepers
english_title: None
format: TV
episodes: 24
status: Finished Airing
average_score: 7
duration: 00:25
start_date: 2000-04-03
end_date: 2000-09-18
studio: Gonzo
source: Game
genres: Comedy|Fantasy|Sci-Fi
all_time_rank: 5178
all_time_popularity: 5092

data_source: jikan
id: 2842
romaji_title: Pokemon Fushigi no Dungeon: Shutsudou Pokemon Kyuujotai Ganbaruzu!
english_title: Pokémon Mystery Dungeon: Team Go-Getters Out of the Gate!
format: TV Special
episodes: 1
status: Finished Airing
average_score: 6.5
duration: 00:20
start_date: 2006-09-08
end_date: None
studio: OLM
source: Game
genres: Adventure|Fantasy
all_time_rank: 8204
all_time_popularity: 6019

data_source: jikan
id: 60580
romaji_title: Xuan Jie Zhi Men
english_title: The Gate of Mystical Realm
format: ONA
episodes: 26
status: Finished Airing
average_score: 7
duration: 00:20
start_date: 2025-11-26
end_date: 2026-05-06
studio: BYMENT
source: Web novel
genres: Action|Adventure|Fantasy
all_time_rank: 5204
all_time_popularity: 15134

data_source: jikan
id: 32888
romaji_title: Sinbad: Mahiru no Yoru to Fushigi no Mon
english_title: Sinbad: Night at High Noon and the Wonder Gate
format: Movie
episodes: 1
status: Finished Airing
average_score: 6.3
duration: 00:51
start_date: 2016-05-14
end_date: None
studio: Nippon Animation
source: Original
genres: Adventure
all_time_rank: 9401
all_time_popularity: 12958

data_source: jikan
id: 48791
romaji_title: Luo Xiaohei Zhanji: Zhongsheng Zhi Men
english_title: The Legend of Luoxiaohei: The Gate of All Living Beings
format: ONA
episodes: 12
status: Finished Airing
average_score: 7.49
duration: 00:08
start_date: 2021-04-24
end_date: 2021-07-17
studio: HMCH
source: Original
genres: Comedy|Supernatural
all_time_rank: 2314
all_time_popularity: 12085

data_source: jikan
id: 32410
romaji_title: Dimension W: W no Tobira Online - Rose no Onayami Soudanshitsu
english_title: Dimension W: W Gate Online - Rose's Counseling Room
format: Special
episodes: 5
status: Finished Airing
average_score: 5.72
duration: 00:03
start_date: 2016-03-25
end_date: 2016-08-26
studio: Studio 3Hz
source: Manga
genres: Sci-Fi
all_time_rank: 12358
all_time_popularity: 6729

"""
    )
