import pandas as pd
from pathlib import Path
from core.exceptions import InvalidFilepathError, AppEmptyDataError
from typing import Any

def valid_filepath(filepath: str) -> Path:
    filepath = filepath.strip().replace(" ", "_")
    filepath_folder = str(Path(filepath).parent)
    if filepath_folder != "storage":
        raise InvalidFilepathError("Error: dataset file must be in the designated folder (example: storage/file.csv)")
    if not filepath.lower().endswith(".csv"):
        raise InvalidFilepathError("dataset file must be a csv file (example: storage/file.csv)")
    return Path(filepath)

class DataIO:
    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath
        
    def add_new_data(self, new_data: dict[str, Any], overwrite: bool = False) -> None:
        self._save_file(new_data, overwrite)
    
    def _read_file(self) -> pd.DataFrame:
        try:
            return pd.read_csv(self.filepath)
        except pd.errors.EmptyDataError:
            raise AppEmptyDataError(f"Failed to read the file because it is empty: {self.filepath}")
    
    def _save_file(self, new_data: dict[str, Any], overwrite: bool = False) -> None:
        df_new_data = pd.DataFrame([new_data])
        
        if overwrite:
            df_new_data.to_csv(self.filepath)
            return
        
        df_previous_data = self._read_file()
        df_merged_data = pd.concat([df_new_data, df_previous_data], ignore_index=True)
        df_merged_data.to_csv(self.filepath)