from argparse import Namespace
import asyncio
from dataclasses import asdict, fields
from typing import Any
from core.normalizer import ResponseNormalizer
from core.exceptions import FetcherError
from core.models.anime_model import AnimeDataModel

async def get_all_by_title(args: Namespace, normalizer: ResponseNormalizer) -> tuple[dict[str, Any], dict[str, Any]]:
        anilist_data, jikan_data = await asyncio.gather(asyncio.to_thread(lambda: normalizer.get_anime_data_by_title(
                                                                          source="anilist", anime_title=args.title, entry_number=args.entry)),
                                                        asyncio.to_thread(lambda: normalizer.get_anime_data_by_title(
                                                                          source="jikan", anime_title=args.title, entry_number=args.entry)))
        return asdict(anilist_data), asdict(jikan_data)
    
async def get_all_by_id(args: Namespace, normalizer: ResponseNormalizer) -> tuple[dict[str, Any], dict[str, Any]]:
        anilist_data, jikan_data = await asyncio.gather(asyncio.to_thread(lambda: normalizer.get_anime_data_by_id(
                                                                          source="anilist", anime_id=args.id)),
                                                        asyncio.to_thread(lambda: normalizer.get_anime_data_by_id(
                                                                          source="jikan", anime_id=args.id)))
        return asdict(anilist_data), asdict(jikan_data)

class FetchCLI:
    def __init__(self, normalizer: ResponseNormalizer) -> None:
        self.normalizer = normalizer
    
    def handle_fetch(self, args: Namespace) -> None:
        if args.title: #search by title
            try:
                if args.source == "all":
                    data1, data2 = asyncio.run(get_all_by_title(args, self.normalizer))
                    for f in fields(AnimeDataModel):
                        print(f"{f.name}: {data1[f.name]} | {data2[f.name]}")
                else:
                    data = asdict(self.normalizer.get_anime_data_by_title(source=args.source, anime_title=args.title, entry_number=args.entry))
                    for key, value in data.items():
                        print(f"{key}: {value}")
            except FetcherError as e:
                print(e)
                return
                
        elif args.id: #search by id
            try:
                if args.source == "all":
                    data1, data2 = asyncio.run(get_all_by_id(args, self.normalizer))
                    for f in fields(AnimeDataModel):
                        print(f"{f.name}: {data1[f.name]} | {data2[f.name]}")
                else:
                    data = asdict(self.normalizer.get_anime_data_by_id(source=args.source, anime_id=args.id))
                    for key, value in data.items():
                        print(f"{key}: {value}")
            except FetcherError as e:
                print(e)
                return