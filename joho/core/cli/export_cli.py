import sys
import asyncio
from argparse import Namespace
from typing import Iterable, Sequence
from joho.core.cli.cli_utils import resolve_index, resolve_sort, all_task_failed
from joho.core.file_handler import DataIO
from joho.core.models.anime_model import AnimeDataModel
from joho.core.models.protocols import NormalizerProtocol
from joho.core.exceptions import FetcherError, EntryIndexError


class ExportCLI:
    def __init__(self, file_handler: DataIO) -> None:
        self.file_handler = file_handler

    async def handle_export_cli(
        self,
        args: Namespace,
        multiple_source: bool,
        normalizers: Sequence[NormalizerProtocol],
    ) -> None:
        try:
            if not multiple_source:
                await self._handle_export_single(args, normalizers[0])
                return
            await self._handle_export_multiple(args, normalizers)
        except FetcherError as e:
            print(e, file=sys.stderr)
            sys.exit(1)
        except EntryIndexError as e:
            print(e, file=sys.stderr)
            sys.exit(1)

    async def _handle_export_single(
        self,
        args: Namespace,
        normalizer: NormalizerProtocol,
    ) -> None:
        sort = resolve_sort(args.sort)
        if args.title:
            if args.save_all:
                data_list = await normalizer.get_all_anime_by_title(
                    args.title, sort, args.max_entry
                )
                self._save_data_list(args.overwrite, data_list)
                return
            data = await normalizer.get_anime_by_title(args.title, sort, args.entry)
            self._save_entry(args.overwrite, data)
        elif args.id:
            data = await normalizer.get_anime_by_id(args.id)
            self._save_entry(args.overwrite, data)

    async def _handle_export_multiple(
        self, args: Namespace, normalizers: Sequence[NormalizerProtocol]
    ) -> None:
        overwrite: bool = args.overwrite
        success_query = 0

        if args.title:
            if args.save_all:
                save_all_coroutines = [
                    n.get_all_anime_by_title(
                        args.title, resolve_sort(args.sort), args.max_entry
                    )
                    for n in normalizers
                ]
                save_all_data_collection = await asyncio.gather(
                    *save_all_coroutines, return_exceptions=True
                )
                for save_all_data_list in save_all_data_collection:
                    if isinstance(save_all_data_list, BaseException):
                        self._show_error(save_all_data_list)
                        continue
                    self._save_data_list(overwrite, save_all_data_list)
                    overwrite = False
                    success_query += 1
            else:
                save_entry_coroutines = [
                    n.get_anime_by_title(
                        args.title, resolve_sort(args.sort), resolve_index(args.entry)
                    )
                    for n in normalizers
                ]
                save_entry_data_list = await asyncio.gather(
                    *save_entry_coroutines, return_exceptions=True
                )
                for save_entry_data in save_entry_data_list:
                    if isinstance(save_entry_data, BaseException):
                        self._show_error(save_entry_data)
                        continue
                    self._save_entry(overwrite, save_entry_data)
                    overwrite = False
                    success_query += 1
            self._show_export_status(success_query, len(normalizers))
        elif args.id:
            by_id_coroutines = [n.get_anime_by_id(args.id) for n in normalizers]
            by_id_data_list = await asyncio.gather(
                *by_id_coroutines, return_exceptions=True
            )
            for by_id_data in by_id_data_list:
                if isinstance(by_id_data, BaseException):
                    self._show_error(by_id_data)
                    continue
                self._save_entry(overwrite, by_id_data)
                overwrite = False
                success_query += 1
            self._show_export_status(success_query, len(by_id_data_list))

        if all_task_failed(success_query):
            sys.exit(1)

    def _save_entry(
        self,
        overwrite: bool,
        entry_data: AnimeDataModel,
    ) -> None:
        self.file_handler.save_data(entry_data, overwrite)

    def _save_data_list(
        self, overwrite: bool, data_list: Iterable[AnimeDataModel]
    ) -> None:
        for data in data_list:
            self._save_entry(overwrite, data)
            overwrite = False

    def _show_error(self, error: BaseException) -> None:
        print(error, file=sys.stderr, end="\n\n")

    def _show_export_status(self, success: int, total_export: int) -> None:
        print(f"{success} / {total_export} exported successfully")
