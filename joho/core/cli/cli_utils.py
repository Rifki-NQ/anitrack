from argparse import Namespace, ArgumentParser
from pathlib import Path
from joho.core.utils import create_default_filepath


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
        return create_default_filepath(default_name)
    return path
