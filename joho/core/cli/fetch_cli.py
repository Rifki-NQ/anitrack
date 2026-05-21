import sys
import asyncio
from argparse import Namespace
from dataclasses import fields
from typing import Sequence
from joho.core.cli.cli_utils import resolve_index, resolve_sort, all_task_failed
from joho.core.models.anime_model import AnimeDataModel
from joho.core.models.protocols import NormalizerProtocol
from joho.core.exceptions import FetcherError, EntryIndexError


class FetchCLI:
    async def handle_fetch_cli(
        self,
        args: Namespace,
        multiple_source: bool,
        normalizers: Sequence[NormalizerProtocol],
    ) -> None:
        try:
            if not multiple_source:
                await self._handle_fetch_single(args, normalizers[0])
                return
            await self._handle_fetch_multiple(args, normalizers)
        except FetcherError as e:
            print(e, file=sys.stderr)
            sys.exit(1)
        except EntryIndexError as e:
            print(e, file=sys.stderr)
            sys.exit(1)

    async def _handle_fetch_single(
        self, args: Namespace, normalizer: NormalizerProtocol
    ) -> None:
        sort = resolve_sort(args.sort)
        if args.title:
            if args.show_title:
                data_list = await normalizer.get_all_anime_by_title(
                    args.title, sort, args.max_entry
                )
                self._show_title(data_list)
                return
            data = await normalizer.get_anime_by_title(args.title, sort, args.entry)
            self._show_entry(data)
        elif args.id:
            data = await normalizer.get_anime_by_id(args.id)
            self._show_entry(data)

    async def _handle_fetch_multiple(
        self, args: Namespace, normalizers: Sequence[NormalizerProtocol]
    ) -> None:
        success_query = 0

        if args.title:
            if args.show_title:
                show_title_coroutines = [
                    n.get_all_anime_by_title(
                        args.title, resolve_sort(args.sort), args.max_entry
                    )
                    for n in normalizers
                ]
                show_title_data_collection = await asyncio.gather(
                    *show_title_coroutines, return_exceptions=True
                )
                for show_title_data_list in show_title_data_collection:
                    if isinstance(show_title_data_list, BaseException):
                        self._show_error(show_title_data_list)
                        continue
                    self._show_title(show_title_data_list)
                    success_query += 1
            else:
                show_entry_coroutines = [
                    n.get_anime_by_title(
                        args.title, resolve_sort(args.sort), resolve_index(args.entry)
                    )
                    for n in normalizers
                ]
                show_entry_data_list = await asyncio.gather(
                    *show_entry_coroutines, return_exceptions=True
                )
                for show_entry_data in show_entry_data_list:
                    if isinstance(show_entry_data, BaseException):
                        self._show_error(show_entry_data)
                        continue
                    self._show_entry(show_entry_data)
                    success_query += 1
            self._show_fetch_status(success_query, len(normalizers))
        elif args.id:
            by_id_coroutines = [n.get_anime_by_id(args.id) for n in normalizers]
            by_id_data_list = await asyncio.gather(
                *by_id_coroutines, return_exceptions=True
            )
            for by_id_data in by_id_data_list:
                if isinstance(by_id_data, BaseException):
                    self._show_error(by_id_data)
                    continue
                self._show_entry(by_id_data)
                success_query += 1
            self._show_fetch_status(success_query, len(by_id_data_list))

        if all_task_failed(success_query):
            sys.exit(1)

    def _show_entry(self, entry_data: AnimeDataModel) -> None:
        for f in fields(entry_data):
            value = getattr(entry_data, f.name)
            print(f"{f.name}: {value}")
        print("")

    def _show_title(self, data_list: list[AnimeDataModel]) -> None:
        print(f"Source: {data_list[0].data_source}")
        print("Romaji title | English title")
        for i, entry_data in enumerate(data_list):
            print(f"{i}. {entry_data.romaji_title} | {entry_data.english_title}")
        print("")

    def _show_error(self, error: BaseException) -> None:
        print(error, file=sys.stderr, end="\n\n")

    def _show_fetch_status(self, success: int, total_export: int) -> None:
        print(f"{success} / {total_export} fetched successfully")
