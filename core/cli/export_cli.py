from argparse import Namespace
from dataclasses import asdict
from pathlib import Path
from core.models.anime_model import AnimeDataModel
from core.normalizer import ResponseNormalizer
from core.file_handler import DataIO
from core.utils import get_all_data_by_title, get_all_data_by_id
from core.exceptions import FetcherError

class ExportCLI:
    def __init__(self, normalizer: ResponseNormalizer, file_handler: DataIO) -> None:
        self.file_handler = file_handler
        self.normalizer = normalizer
        
    def handle_export(self, args: Namespace) -> None:
        if args.title: #search by title
            self._handle_args_title(args)
                
        elif args.id: #search by id
            self._handle_args_title(args)
        
    def _handle_args_title(self, args: Namespace) -> None:
        try:
            if args.source == "all":
                self._handle_source_all_by_title(args)
            elif args.save_all:
                data_list = self.normalizer.get_all_anime_data_by_title(source=args.source, anime_title=args.title)
                self._save_data_list(data_list, path=args.path, overwrite=args.overwrite)
            else:
                data = asdict(self.normalizer.get_anime_data_by_title(source=args.source, anime_title=args.title, entry_number=args.entry))
                self.file_handler.add_new_data(new_data=data, filepath=args.path, overwrite=args.overwrite)
        except FetcherError as e:
            print(e)
            return
        
    def _handle_args_id(self, args: Namespace) -> None:
        try:
            if args.source == "all":
                self._handle_source_all_by_id(args)
            else:
                data = asdict(self.normalizer.get_anime_data_by_id(source=args.source, anime_id=args.id))
                self.file_handler.add_new_data(new_data=data, filepath=args.path, overwrite=args.overwrite)
        except FetcherError as e:
            print(e)
            return
        
    def _handle_source_all_by_title(self, args: Namespace) -> None:
        data_collection = get_all_data_by_title(args, self.normalizer)
        overwrite = args.overwrite
        for data_list in data_collection:
            self._save_data_list(data_list, args.path, overwrite)
            overwrite = False

    def _handle_source_all_by_id(self, args: Namespace) -> None:
        data1, data2 = get_all_data_by_id(args, self.normalizer)
        data_list = [data1, data2]
        self._save_data_list(data_list, args.path, args.overwrite)

    def _save_data_list(self, data_list: list[AnimeDataModel], path: Path, overwrite: bool) -> None:
        for data in data_list:
            self.file_handler.add_new_data(asdict(data), path, overwrite)
            overwrite = False