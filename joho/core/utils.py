from argparse import ArgumentTypeError
from pathlib import Path

DEFAULT_FILEPATH_FOLDER = "storage/"
VALID_FILE_EXTENSION = ".csv"


def create_default_filepath(raw_name: str | int) -> Path:
    if isinstance(raw_name, int):
        raw_name = str(raw_name)
    filename = raw_name.replace(" ", "_")
    filepath = DEFAULT_FILEPATH_FOLDER + filename + VALID_FILE_EXTENSION
    return Path(filepath)


def valid_filepath(filepath: str) -> Path:
    path = Path(filepath)
    if path.suffix.lower() != ".csv":
        raise ArgumentTypeError("dataset file must be a csv file (example: data.csv)")
    return path.with_stem(path.stem.replace(" ", "_"))
