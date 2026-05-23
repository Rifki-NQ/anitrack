import pytest
import argparse
from pathlib import Path
from joho.main import build_parser
from joho.core.cli.read_cli import ReadCLI
from joho.core.file_handler import DataIO


@pytest.fixture
def parser() -> argparse.ArgumentParser:
    return build_parser()


@pytest.fixture
def read(
    parser: argparse.ArgumentParser, request: pytest.FixtureRequest
) -> argparse.Namespace:
    path: str = request.param
    return parser.parse_args(["read", "--path", path])


@pytest.mark.parametrize("read", ["not_exist.csv"], indirect=True)
def test_read_file_not_exist(
    capsys: pytest.CaptureFixture[str], read: argparse.Namespace
) -> None:
    path: Path = read.path
    read_cli = ReadCLI(DataIO(path))
    with pytest.raises(SystemExit) as exit_info:
        read_cli.handle_read_cli(read)
    captured = capsys.readouterr()
    assert not path.exists()
    assert exit_info.value.code == 1
    assert captured.err == "Error: file does not exist\n"


@pytest.mark.parametrize("read", ["tests/mock_data/empty_data.csv"], indirect=True)
def test_read_file_empty(
    capsys: pytest.CaptureFixture[str], read: argparse.Namespace
) -> None:
    path: Path = read.path
    read_cli = ReadCLI(DataIO(path))
    with pytest.raises(SystemExit) as exit_info:
        read_cli.handle_read_cli(read)
    captured = capsys.readouterr()
    assert path.exists()
    assert exit_info.value.code == 1
    assert captured.err == "Error: file is empty\n"


@pytest.mark.parametrize("read", ["tests/mock_data/only_whitespace.csv"], indirect=True)
def test_read_file_only_whitespace(
    capsys: pytest.CaptureFixture[str], read: argparse.Namespace
) -> None:
    path: Path = read.path
    read_cli = ReadCLI(DataIO(path))
    with pytest.raises(SystemExit) as exit_info:
        read_cli.handle_read_cli(read)
    captured = capsys.readouterr()
    assert path.exists()
    assert exit_info.value.code == 1
    assert captured.err == "Error: file is empty\n"


@pytest.mark.parametrize("read", ["tests/mock_data/only_headers.csv"], indirect=True)
def test_read_file_only_headers(
    capsys: pytest.CaptureFixture[str], read: argparse.Namespace
) -> None:
    path: Path = read.path
    read_cli = ReadCLI(DataIO(path))
    with pytest.raises(SystemExit) as exit_info:
        read_cli.handle_read_cli(read)
    captured = capsys.readouterr()
    assert path.exists()
    assert exit_info.value.code == 1
    assert captured.err == "Error: file is empty\n"


@pytest.mark.parametrize(
    "read", ["tests/mock_data/data_with_missing_header.csv"], indirect=True
)
def test_read_file_missing_header(
    capsys: pytest.CaptureFixture[str], read: argparse.Namespace
) -> None:
    path: Path = read.path
    read_cli = ReadCLI(DataIO(path))
    with pytest.raises(SystemExit) as exit_info:
        read_cli.handle_read_cli(read)
    captured = capsys.readouterr()
    assert path.exists()
    assert exit_info.value.code == 1
    assert (
        captured.err == "Error: missing header from the file: {'all_time_popularity'}\n"
    )


@pytest.mark.parametrize(
    "read", ["tests/mock_data/data_with_extra_header.csv"], indirect=True
)
def test_read_file_extra_header(
    capsys: pytest.CaptureFixture[str], read: argparse.Namespace
) -> None:
    path: Path = read.path
    read_cli = ReadCLI(DataIO(path))
    with pytest.raises(SystemExit) as exit_info:
        read_cli.handle_read_cli(read)
    captured = capsys.readouterr()
    assert path.exists()
    assert exit_info.value.code == 1
    assert captured.err == "Error: invalid header: {'extra_header'}\n"
