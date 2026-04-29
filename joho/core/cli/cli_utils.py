import asyncio
from argparse import Namespace, ArgumentParser
from pathlib import Path
from joho.core.models.anime_model import AnimeDataModel
from joho.core.models.protocols import NormalizerProtocol
from joho.core.utils import create_defaulf_filepath


def validate_args_fetch(parser: ArgumentParser, args: Namespace) -> None:
    if args.title is None and (args.entry is not None or args.show_title):
        parser.error("--entry and --show-title can only be used with --title")
    elif args.max_entry is not None and not args.show_title:
        parser.error("--max-entry can only be used with --show-title")


def validate_args_export(parser: ArgumentParser, args: Namespace) -> None:
    if args.title is None and (args.entry is not None or args.save_all):
        parser.error("--entry and --save-all can only be used with --title")
    elif args.max_entry is not None and not args.save_all:
        parser.error("--max-entry can only be used with --save-all")


def validate_export_path(path: Path | None, default_name: str | int) -> Path:
    if path is None:
        return create_defaulf_filepath(default_name)
    return path


def get_all_data_by_title(
    args: Namespace, *normalizers: NormalizerProtocol
) -> list[list[AnimeDataModel] | BaseException]:
    return asyncio.run(_get_all_by_title(args, *normalizers))


def get_all_data_by_id(
    args: Namespace, *normalizers: NormalizerProtocol
) -> list[AnimeDataModel | BaseException]:
    return asyncio.run(_get_all_by_id(args, *normalizers))


async def _get_all_by_title(
    args: Namespace, *normalizers: NormalizerProtocol
) -> list[list[AnimeDataModel] | BaseException]:
    all_thread = [
        asyncio.to_thread(normalizer.get_all_anime_by_title, args.title, args.max_entry)
        for normalizer in normalizers
    ]
    all_data = await asyncio.gather(*all_thread, return_exceptions=True)
    return all_data


async def _get_all_by_id(
    args: Namespace, *normalizers: NormalizerProtocol
) -> list[AnimeDataModel | BaseException]:
    all_thread = [
        asyncio.to_thread(normalizer.get_anime_by_id, args.id)
        for normalizer in normalizers
    ]
    all_data = await asyncio.gather(*all_thread, return_exceptions=True)
    return all_data
