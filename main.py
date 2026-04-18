import argparse
from core.models.anime_model import DATA_SOURCES, VALID_DATA_SOURCES
from core.cli.fetch_cli import FetchCLI
from core.cli.export_cli import ExportCLI
from core.fetchers.fetcher_factory import create_fetcher
from core.normalizers.base_normalizer import BaseNormalizer
from core.normalizers.normalizer_factory import create_normalizer
from core.file_handler import valid_filepath
from core.file_handler import DataIO

VALID_COMMANDS = {"fetch", "export"}

def _create_dependency(command: str, source: DATA_SOURCES
                       ) -> BaseNormalizer | tuple[BaseNormalizer, DataIO]:
    normalizer = create_normalizer(source, create_fetcher(source))
    if command == "fetch":
        return normalizer
    elif command == "export":
        return (normalizer, DataIO())
    else:
        raise ValueError(f"command not recognized: {command}")

def _create_dependency_all_source(command: str
                                  ) -> list[BaseNormalizer] | tuple[list[BaseNormalizer], DataIO]:
    normalizers: list[BaseNormalizer] = []
    for source in VALID_DATA_SOURCES:
        normalizers.append(create_normalizer(source, create_fetcher(source)))
    if command == "fetch":
        return normalizers
    elif command == "export":
        return normalizers, DataIO()
    else:
        raise ValueError(f"command not recognized: {command}")

def main_parser():
    VALID_SOURCES = {"anilist", "jikan", "all"}
    parser = argparse.ArgumentParser(prog="anitrack")
    subparsers = parser.add_subparsers(dest="command")

    #subcommand fetch
    fetch_parser = subparsers.add_parser("fetch", description="fetch anime data")
    fetch_parser.add_argument("--source", choices=VALID_SOURCES, required=True)
    fetch_parser.add_argument("--max-entry", type=int, default=None)
    fetch_entry_group = fetch_parser.add_mutually_exclusive_group(required=False)
    fetch_entry_group.add_argument("--entry", type=int, default=None)
    fetch_entry_group.add_argument("--show-title", action="store_true", default=False)
    search_by_group = fetch_parser.add_mutually_exclusive_group(required=True)
    search_by_group.add_argument("--title", type=str)
    search_by_group.add_argument("--id", type=int)
    
    #subcommand export
    export_parser =subparsers.add_parser("export", description="fetch then save anime data")
    export_parser.add_argument("--source", choices=VALID_SOURCES, required=True)
    search_by_group = export_parser.add_mutually_exclusive_group(required=True)
    search_by_group.add_argument("--title", type=str)
    search_by_group.add_argument("--id", type=int)
    export_entry_group = export_parser.add_mutually_exclusive_group(required=False)
    export_entry_group.add_argument("--entry", type=int, default=0)
    export_entry_group.add_argument("--save-all", action="store_true", default=False)
    export_parser.add_argument("--path", type=valid_filepath, required=True)
    export_parser.add_argument("--overwrite", action="store_true", default=False)
    export_parser.add_argument("--max-entry", type=int, default=None)

    args = parser.parse_args()

    if args.command == "fetch":
        if args.title is None and (args.entry is not None or args.show_title):
            fetch_parser.error("--entry and --show-title can only be used with --title")
        elif args.max_entry is not None and not args.show_title:
            fetch_parser.error("--max-entry can only be used with --show-title")

        if args.source == "all":
            dependency = _create_dependency_all_source("fetch")
        else:
            dependency = _create_dependency("fetch", args.source)
        fetch_cli = FetchCLI(dependency)
        fetch_cli.handle_fetch(args)
        
    elif args.command == "export":
        if args.title is None and (args.entry is not None or args.save_all):
            export_parser.error("--entry and --save-all can only be used with --title")
        elif args.max_entry is not None and not args.save_all:
            export_parser.error("--max-entry can only be used with --save-all")

        export_cli = ExportCLI()
        export_cli.handle_export(args)
    else:
        parser.print_help()
            
if __name__ == "__main__":
    main_parser()