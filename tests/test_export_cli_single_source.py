import pytest
import argparse
from pathlib import Path
from joho.main import build_parser
from joho.core.cli.export_cli import ExportCLI
from joho.core.cli.cli_utils import validate_export_path
from joho.core.normalizers.normalizer_factory import create_normalizer
from joho.core.models.protocols import NormalizerProtocol
from joho.core.file_handler import DataIO
from tests.fetchers_mock_data import MockJikanFetcher

# detailed file content / values tests are skipped in this test
# since test_file_handler.py already handles it


@pytest.fixture
def parser() -> argparse.ArgumentParser:
    return build_parser()


@pytest.fixture
def temporary_path(tmp_path: Path) -> Path:
    return tmp_path / "data.csv"


@pytest.fixture
def single_normalizer() -> list[NormalizerProtocol]:
    return [create_normalizer("jikan", MockJikanFetcher())]


def count_lines(path: Path) -> int:
    with open(path, "rb") as f:
        count = sum(1 for _ in f)
    return count


@pytest.fixture
def export_single_by_title(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "jikan",
            "--title",
            "attack on titan",
            "--path",
            str(temporary_path),
        ]
    )


@pytest.fixture
def export_single_by_id(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        ["export", "--source", "jikan", "--id", "16498", "--path", str(temporary_path)]
    )


@pytest.fixture
def export_single_no_path(parser: argparse.ArgumentParser) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "jikan",
            "--title",
            "attack on titan",
        ]
    )


@pytest.fixture
def export_single_entry(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "jikan",
            "--title",
            "attack on titan",
            "--path",
            str(temporary_path),
            "--entry",
            "2",
        ]
    )


@pytest.fixture
def export_single_save_all(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "jikan",
            "--title",
            "attack on titan",
            "--path",
            str(temporary_path),
            "--save-all",
        ]
    )


@pytest.fixture
def export_single_max_entry(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "jikan",
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
def export_single_overwrite_by_title(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "jikan",
            "--title",
            "attack on titan",
            "--path",
            str(temporary_path),
            "--overwrite",
        ]
    )


@pytest.fixture
def export_single_overwrite_by_id(
    parser: argparse.ArgumentParser, temporary_path: Path
) -> argparse.Namespace:
    return parser.parse_args(
        [
            "export",
            "--source",
            "jikan",
            "--id",
            "16498",
            "--path",
            str(temporary_path),
            "--overwrite",
        ]
    )


# uses jikan mocked data
async def test_export_single_by_title(
    export_single_by_title: argparse.Namespace,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    """file is expected to be two line, which is header and one row of anime entry"""
    path: Path = export_single_by_title.path
    export_cli = ExportCLI(DataIO(path))
    await export_cli.handle_export_cli(export_single_by_title, False, single_normalizer)
    assert count_lines(path) == 2


# uses jikan mocked data
async def test_export_single_by_id(
    export_single_by_id: argparse.Namespace, single_normalizer: list[NormalizerProtocol]
) -> None:
    """file is expected to be two line, which is header and one row of anime entry"""
    path: Path = export_single_by_id.path
    export_cli = ExportCLI(DataIO(path))
    await export_cli.handle_export_cli(export_single_by_id, False, single_normalizer)
    assert count_lines(path) == 2


# uses jikan mocked data
async def test_export_single_no_path(
    export_single_no_path: argparse.Namespace,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    """
    test logic: validate_export_path, when no --path is provided,
    it will create a new file with the name of either --title or --id inside storage/ folder

    file is expected to be two line, which is header and one row of anime entry.
    file will be deleted after this test.
    """
    path: Path = validate_export_path(
        export_single_no_path.path, default_name=export_single_no_path.title
    )
    try:
        export_cli = ExportCLI(DataIO(path))
        await export_cli.handle_export_cli(
            export_single_no_path, False, single_normalizer
        )
        assert path.exists()
        assert str(path.parent) == "storage"
        assert count_lines(path) == 2
    finally:
        path.unlink(missing_ok=True)


# uses jikan mocked data
async def test_fetch_single_entry(
    export_single_entry: argparse.Namespace, single_normalizer: list[NormalizerProtocol]
) -> None:
    """
    test flag: --entry combined with --title

    file is expected to be two line, which is header and one row of anime entry
    """
    path: Path = export_single_entry.path
    export_cli = ExportCLI(DataIO(path))
    await export_cli.handle_export_cli(export_single_entry, False, single_normalizer)
    assert count_lines(path) == 2


# uses jikan mocked data
async def test_export_single_save_all(
    export_single_save_all: argparse.Namespace,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    """
    test flag: --save-all combined with --title

    file is expected to be four line, which is header and three row of anime entry
    """
    path: Path = export_single_save_all.path
    export_cli = ExportCLI(DataIO(path))
    await export_cli.handle_export_cli(export_single_save_all, False, single_normalizer)
    assert count_lines(path) == 4


# uses jikan mocked data
async def test_export_single_max_entry(
    export_single_max_entry: argparse.Namespace,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    """
    test flag: --max-entry combined with --save-all and --title

    file is expected to be three line, which is header and two row of anime entry
    """
    path: Path = export_single_max_entry.path
    export_cli = ExportCLI(DataIO(path))
    await export_cli.handle_export_cli(
        export_single_max_entry, False, single_normalizer
    )
    assert count_lines(path) == 3


# uses jikan mocked data
async def test_export_single_with_overwrite_by_title(
    export_single_overwrite_by_title: argparse.Namespace,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    """
    test flag: --overwrite with --title
    test logic: export three times, file content is expected to be overwritten for each export

    file is expected to be two line for each iteration, which is header and one row of anime entry
    """
    path: Path = export_single_overwrite_by_title.path
    export_cli = ExportCLI(DataIO(path))
    for _ in range(3):
        await export_cli.handle_export_cli(
            export_single_overwrite_by_title, False, single_normalizer
        )
        assert count_lines(path) == 2


# uses jikan mocked data
async def test_export_single_without_overwrite_by_title(
    export_single_by_title: argparse.Namespace,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    """
    test logic: export two times, new data is expected to be appended to existing data

    file is expected to be two lines on first iteration, three lines on second iteration
    """
    path: Path = export_single_by_title.path
    export_cli = ExportCLI(DataIO(path))
    for i in [2, 3]:
        await export_cli.handle_export_cli(
            export_single_by_title, False, single_normalizer
        )
        assert count_lines(path) == i


# uses jikan mocked data
async def test_export_single_with_overwrite_by_id(
    export_single_overwrite_by_id: argparse.Namespace,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    """
    test flag: --overwrite with --id
    test logic: export three times, file content is expected to be overwritten for each export

    file is expected to be two line for each iteration, which is header and one row of anime entry
    """
    path: Path = export_single_overwrite_by_id.path
    export_cli = ExportCLI(DataIO(path))
    for _ in range(3):
        await export_cli.handle_export_cli(
            export_single_overwrite_by_id, False, single_normalizer
        )
        assert count_lines(path) == 2


# uses jikan mocked data
async def test_export_single_without_overwrite_by_id(
    export_single_by_id: argparse.Namespace,
    single_normalizer: list[NormalizerProtocol],
) -> None:
    """
    test logic: export two times, new data is expected to be appended to existing data

    file is expected to be two lines on first iteration, three lines on second iteration
    """
    path: Path = export_single_by_id.path
    export_cli = ExportCLI(DataIO(path))
    for i in [2, 3]:
        await export_cli.handle_export_cli(
            export_single_by_id, False, single_normalizer
        )
        assert count_lines(path) == i
