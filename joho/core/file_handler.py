import csv
from pathlib import Path
from dataclasses import fields, asdict
from joho.core.models.anime_model import AnimeDataModel
from joho.core.exceptions import FileNotExistError, FileEmptyError


class DataIO:
    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath

    def save_data(self, data: AnimeDataModel, overwrite: bool) -> None:
        overwrite_map = {True: "w", False: "a"}
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

        is_empty_file = self._file_empty() if self._file_exist() else True
        with open(self.filepath, mode=overwrite_map[overwrite], newline="") as f:
            fieldnames = [adm.name for adm in fields(AnimeDataModel)]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if overwrite or is_empty_file:
                writer.writeheader()
            writer.writerow(asdict(data))

    def read_data(self) -> list[dict[str, str]]:
        if not self._file_exist():
            raise FileNotExistError("Error: file does not exist")
        elif self._file_empty():
            raise FileEmptyError("Error: file is empty")
        entries: list[dict[str, str]] = []
        with open(self.filepath, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                entries.append(row)
        return entries

    def _file_exist(self) -> bool:
        return self.filepath.exists()

    def _file_empty(self) -> bool:
        return self.filepath.stat().st_size == 0
