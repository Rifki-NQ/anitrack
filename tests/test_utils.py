import pytest
from argparse import ArgumentTypeError
from pathlib import Path
from joho.core.utils import create_default_filepath, valid_filepath


@pytest.mark.parametrize(
    "raw_name, expected",
    [
        ("steins gate", Path("storage/steins_gate.csv")),
        ("attack on titan", Path("storage/attack_on_titan.csv")),
        ("Gachiakuta", Path("storage/Gachiakuta.csv")),
        ("16498", Path("storage/16498.csv")),
    ],
)
def test_create_default_filepath(raw_name: str, expected: Path) -> None:
    """
    test if create_default_filepath convert spaces into underscores for the raw_name,
    put the converted raw_name to storage/ and add .csv as the suffix

    this helper function is triggered when args.path is None
    which means user did not provided the --path in the command
    """
    converted = create_default_filepath(raw_name)
    assert converted == expected


@pytest.mark.parametrize(
    "raw_path, expected",
    [
        ("my storage/steins gate.csv", Path("my storage/steins_gate.csv")),
        ("my_storage/attack on titan.CSV", Path("my_storage/attack_on_titan.csv")),
        ("my_storage/Gachiakuta.cSv", Path("my_storage/Gachiakuta.csv")),
        ("my_storage/16498.csV", Path("my_storage/16498.csv")),
    ],
)
def test_valid_filepath(raw_path: str, expected: Path) -> None:
    """
    test if valid_filepath convert user inputted raw_path into Path object
    with the filename spaces converted into undescores
    and the suffix normalized into lowercases
    """
    converted = valid_filepath(raw_path)
    assert converted == expected


@pytest.mark.parametrize(
    "raw_path",
    [
        "my storage/steins gate.txt",
        "my_storage/16498",
        "my_storage/ ",
        "my_storage/.csv",  # empty stem, treated as invalid
    ],
)
def test_not_valid_filepath(raw_path: str) -> None:
    """
    test if valid_filepath raises error when user inputted invalid --path
    which is when the --path is not a csv file
    """
    with pytest.raises(ArgumentTypeError) as exc_info:
        valid_filepath(raw_path)
    assert (
        exc_info.value.args[0] == "dataset file must be a csv file (example: data.csv)"
    )
