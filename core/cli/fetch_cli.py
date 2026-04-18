from argparse import Namespace
from dataclasses import asdict, fields
from core.cli.cli_utils import get_all_data_by_title, get_all_data_by_id
from core.models.anime_model import AnimeDataModel
from core.models.protocols import NormalizerProtocol
from core.exceptions import FetcherError

class FetchCLI:
    def __init__(self, *normalizers: NormalizerProtocol) -> None:
        self.normalizer = normalizers[0]
        if len(normalizers) > 1:
            self.extra_normalizer = normalizers[1:]
    
    def handle_fetch(self, args: Namespace) -> None:
        if args.title: #search by title
            self._handle_args_title(args)
                
        elif args.id: #search by id
            self._handle_args_id(args)
            
    def _handle_args_title(self, args: Namespace) -> None:
        try:
            if args.source == "all": #handle --source all
                normalizers = filter(None, [self.normalizer, *self.extra_normalizer])
                data_collection = get_all_data_by_title(args, *normalizers)
                self._handle_source_all_by_title(args, data_collection)
            elif args.show_title:
                data_list = self.normalizer.get_all_anime_by_title(args.title)
                self._handle_show_title(data_list)
            else:
                data = asdict(self.normalizer.get_anime_by_title(args.title, args.entry))
                for key, value in data.items():
                    print(f"{key}: {value}")
        except FetcherError as e:
            print(e)
        except IndexError:
            print(f"Error: --entry index out of range for title: {args.title}")
            
    def _handle_args_id(self, args: Namespace) -> None:
        try:
            if args.source == "all": #handle --source all
                self._handle_source_all_by_id(args)
            else:
                data = asdict(self.normalizer.get_anime_by_id(args.id))
                for key, value in data.items():
                    print(f"{key}: {value}")
        except FetcherError as e:
            print(e)
            return
        
    def _handle_source_all_by_title(self, args: Namespace, data_collection: list[list[AnimeDataModel]]) -> None:
        if args.show_title:
            self._handle_show_title_all(data_collection)
            return
        entry_num: int = args.entry
        for f in fields(AnimeDataModel):
            print(f"{f.name}: {asdict(data_collection[0][entry_num])[f.name]} | {asdict(data_collection[1][entry_num])[f.name]}")
    
    def _handle_source_all_by_id(self, args: Namespace) -> None:
        data1, data2 = get_all_data_by_id(args, self.normalizer)
        for f in fields(AnimeDataModel):
            print(f"{f.name}: {asdict(data1)[f.name]} | {asdict(data2)[f.name]}")
    
    def _handle_show_title(self, data_list: list[AnimeDataModel]) -> None:
        print(f"Source: {data_list[0].source}")
        print("Entry no: Romaji title | English title")
        for i, data in enumerate(data_list):
            print(f"{i:>7}: {data.romaji_title} | {data.english_title}")
            
    def _handle_show_title_all(self, data_collection: list[list[AnimeDataModel]]) -> None:
        for data_list in data_collection:
            self._handle_show_title(data_list)