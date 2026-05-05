from argparse import Namespace
from joho.core.file_handler import DataIO
from joho.core.exceptions import FileHandlerError


class ReadCLI:
    MAXIMUM_ENTRIES_PER_PAGE = 10

    def __init__(self, file_handler: DataIO) -> None:
        self.file_handler = file_handler

    def handle_read_cli(self, args: Namespace) -> None:
        try:
            all_data = self.file_handler.read_data()
        except FileHandlerError as e:
            print(e)
            return
        if args.entry is not None:
            entry_num: int = args.entry
            try:
                self._show_entry(all_data[entry_num])
            except IndexError:
                print(
                    f"Error: out of bound entry index: {args.entry}, for file: {self.file_handler.filepath}"
                )
            return
        elif args.show_title:
            self._show_title(all_data)
            return
        self._show_entries(all_data, limit=args.limit)

    def _show_entry(self, entry_data: dict[str, str | None]) -> None:
        for key, value in entry_data.items():
            print(f"{key}: {value}")

    def _show_entries(
        self, data_list: list[dict[str, str | None]], limit: int | None
    ) -> None:
        effective_limit = limit if limit is not None else self.MAXIMUM_ENTRIES_PER_PAGE
        for i, entry in enumerate(data_list, 1):
            self._show_entry(entry)
            print()
            if effective_limit > 0 and i >= effective_limit:
                break

    def _show_title(self, data_list: list[dict[str, str | None]]) -> None:
        print("Data source | Romaji title | English title")
        for i, entry in enumerate(data_list):
            print(
                f"{i}. {entry['data_source']} | {entry['romaji_title']} | {entry['english_title']}"
            )
