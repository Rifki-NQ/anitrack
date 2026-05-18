import pytest
import argparse
from pathlib import Path
from joho.main import build_parser
from joho.core.cli.export_cli import ExportCLI
from joho.core.cli.cli_utils import validate_export_path
from joho.core.normalizers.normalizer_factory import create_normalizer
from joho.core.models.protocols import NormalizerProtocol
from joho.core.file_handler import DataIO
from tests.mock_classes.mock_anilist_fetcher import MockAnilistFetcherNormal
from tests.mock_classes.mock_jikan_fetcher import MockJikanFetcherNormal

# detailed file content / values tests are skipped in this test
# since test_file_handler.py already handles it


@pytest.fixture
def parser() -> argparse.ArgumentParser:
    return build_parser()


@pytest.fixture
def temporary_path(tmp_path: Path) -> Path:
    return tmp_path / "data.csv"


@pytest.fixture
def multiple_normalizers() -> list[NormalizerProtocol]:
    return [
        create_normalizer("anilist", MockAnilistFetcherNormal()),
        create_normalizer("jikan", MockJikanFetcherNormal()),
    ]


def count_lines(path: Path) -> int:
    with open(path, "rb") as f:
        count = sum(1 for _ in f)
    return count


@pytest.fixture
def export_multi_by_title(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "all",
            "--title",
            "attack on titan",
            "--path",
            str(temporary_path),
        ]
    )


@pytest.fixture
def export_multi_by_id(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        ["export", "--source", "all", "--id", "16498", "--path", str(temporary_path)]
    )


@pytest.fixture
def export_multi_no_path(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "all",
            "--title",
            "attack on titan",
        ]
    )


@pytest.fixture
def export_multi_entry(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "all",
            "--title",
            "attack on titan",
            "--path",
            str(temporary_path),
            "--entry",
            "2",
        ]
    )


@pytest.fixture
def export_multi_save_all(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "all",
            "--title",
            "attack on titan",
            "--path",
            str(temporary_path),
            "--save-all",
        ]
    )


@pytest.fixture
def export_multi_max_entry(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "all",
            "--title",
            "attack on titan",
            "--path",
            str(temporary_path),
            "--save-all",
            "--max-entry",
            "2",
        ]
    )


@pytest.fixture
def export_multi_overwrite_by_title(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "all",
            "--title",
            "attack on titan",
            "--path",
            str(temporary_path),
            "--overwrite",
        ]
    )


@pytest.fixture
def export_multi_overwrite_by_id(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "all",
            "--id",
            "16498",
            "--path",
            str(temporary_path),
            "--overwrite",
        ]
    )


# uses jikan mocked data
async def test_export_multi_by_title(
    export_multi_by_title: argparse.Namespace,
    multiple_normalizers: list[NormalizerProtocol],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """file is expected to be three line, which is header and two row of anime entry"""
    path: Path = export_multi_by_title.path
    export_cli = ExportCLI(DataIO(path))
    await export_cli.handle_export_cli(
        export_multi_by_title, True, multiple_normalizers
    )
    captured = capsys.readouterr()
    assert count_lines(path) == 3
    assert captured.out == "2 / 2 exported successfully\n"


# uses jikan mocked data
async def test_export_multi_by_id(
    export_multi_by_id: argparse.Namespace,
    multiple_normalizers: list[NormalizerProtocol],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """file is expected to be three line, which is header and two row of anime entry"""
    path: Path = export_multi_by_id.path
    export_cli = ExportCLI(DataIO(path))
    await export_cli.handle_export_cli(export_multi_by_id, True, multiple_normalizers)
    captured = capsys.readouterr()
    assert count_lines(path) == 3
    assert captured.out == "2 / 2 exported successfully\n"


# uses jikan mocked data
async def test_export_multi_no_path(
    export_multi_no_path: argparse.Namespace,
    multiple_normalizers: list[NormalizerProtocol],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    test logic: validate_export_path, when no --path is provided,
    it will create a new file with the name of either --title or --id inside storage/ folder

    file is expected to be three line, which is header and two row of anime entry.
    file will be deleted after this test.
    """
    path: Path = validate_export_path(
        export_multi_no_path.path, default_name=export_multi_no_path.title
    )
    try:
        export_cli = ExportCLI(DataIO(path))
        await export_cli.handle_export_cli(
            export_multi_no_path, True, multiple_normalizers
        )
        captured = capsys.readouterr()
        assert path.exists()
        assert str(path.parent) == "storage"
        assert count_lines(path) == 3
        assert captured.out == "2 / 2 exported successfully\n"
    finally:
        path.unlink(missing_ok=True)


# uses jikan mocked data
async def test_export_multi_entry(
    export_multi_entry: argparse.Namespace,
    multiple_normalizers: list[NormalizerProtocol],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    test flag: --entry combined with --title

    file is expected to be three line, which is header and two row of anime entry
    """
    path: Path = export_multi_entry.path
    export_cli = ExportCLI(DataIO(path))
    await export_cli.handle_export_cli(export_multi_entry, True, multiple_normalizers)
    captured = capsys.readouterr()
    assert count_lines(path) == 3
    assert captured.out == "2 / 2 exported successfully\n"


# uses jikan mocked data
async def test_export_multi_save_all(
    export_multi_save_all: argparse.Namespace,
    multiple_normalizers: list[NormalizerProtocol],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    test flag: --save-all combined with --title

    file is expected to be 24 line, which is header and 23 row of anime entry
    """
    path: Path = export_multi_save_all.path
    export_cli = ExportCLI(DataIO(path))
    await export_cli.handle_export_cli(
        export_multi_save_all, True, multiple_normalizers
    )
    captured = capsys.readouterr()
    assert count_lines(path) == 24
    assert captured.out == "2 / 2 exported successfully\n"


# uses jikan mocked data
async def test_export_multi_max_entry(
    export_multi_max_entry: argparse.Namespace,
    multiple_normalizers: list[NormalizerProtocol],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    test flag: --max-entry combined with --save-all and --title

    file is expected to be five line, which is header and four row of anime entry
    """
    path: Path = export_multi_max_entry.path
    export_cli = ExportCLI(DataIO(path))
    await export_cli.handle_export_cli(
        export_multi_max_entry, True, multiple_normalizers
    )
    captured = capsys.readouterr()
    assert count_lines(path) == 5
    assert captured.out == "2 / 2 exported successfully\n"


# uses jikan mocked data
async def test_export_multi_with_overwrite_by_title(
    export_multi_overwrite_by_title: argparse.Namespace,
    multiple_normalizers: list[NormalizerProtocol],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    test flag: --overwrite with --title
    test logic: export three times, file content is expected to be overwritten for each export

    file is expected to be three line for each iteration, which is header and two row of anime entry
    """
    path: Path = export_multi_overwrite_by_title.path
    export_cli = ExportCLI(DataIO(path))
    for _ in range(3):
        await export_cli.handle_export_cli(
            export_multi_overwrite_by_title, True, multiple_normalizers
        )
        captured = capsys.readouterr()
        assert count_lines(path) == 3
        assert captured.out == "2 / 2 exported successfully\n"


# uses jikan mocked data
async def test_export_multi_without_overwrite_by_title(
    export_multi_by_title: argparse.Namespace,
    multiple_normalizers: list[NormalizerProtocol],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    test logic: export two times, new data is expected to be appended to existing data

    file is expected to be three lines on first iteration, five lines on second iteration
    """
    path: Path = export_multi_by_title.path
    export_cli = ExportCLI(DataIO(path))
    for i in [3, 5]:
        await export_cli.handle_export_cli(
            export_multi_by_title, True, multiple_normalizers
        )
        captured = capsys.readouterr()
        assert count_lines(path) == i
        assert captured.out == "2 / 2 exported successfully\n"


# uses jikan mocked data
async def test_export_multi_with_overwrite_by_id(
    export_multi_overwrite_by_id: argparse.Namespace,
    multiple_normalizers: list[NormalizerProtocol],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    test flag: --overwrite with --id
    test logic: export three times, file content is expected to be overwritten for each export

    file is expected to be three line for each iteration, which is header and two row of anime entry
    """
    path: Path = export_multi_overwrite_by_id.path
    export_cli = ExportCLI(DataIO(path))
    for _ in range(3):
        await export_cli.handle_export_cli(
            export_multi_overwrite_by_id, True, multiple_normalizers
        )
        captured = capsys.readouterr()
        assert count_lines(path) == 3
        assert captured.out == "2 / 2 exported successfully\n"


# uses jikan mocked data
async def test_export_multi_without_overwrite_by_id(
    export_multi_by_id: argparse.Namespace,
    multiple_normalizers: list[NormalizerProtocol],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    test logic: export two times, new data is expected to be appended to existing data

    file is expected to be three lines on first iteration, five lines on second iteration
    """
    path: Path = export_multi_by_id.path
    export_cli = ExportCLI(DataIO(path))
    for i in [3, 5]:
        await export_cli.handle_export_cli(
            export_multi_by_id, True, multiple_normalizers
        )
        captured = capsys.readouterr()
        assert count_lines(path) == i
        assert captured.out == "2 / 2 exported successfully\n"
