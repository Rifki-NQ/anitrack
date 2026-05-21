class AppError(Exception):
    """Base class exception for all app related error"""

    pass


class FetcherError(AppError):
    """Raised when there is fetcher related error"""

    pass


class InvalidDataSource(FetcherError):
    """Raised when the data source is invalid"""

    pass


class AppConnectionError(FetcherError):
    """Raised when there is connection related error"""

    pass


class AnimeNotFoundError(FetcherError):
    """Raised when the queried anime is not found"""

    def __init__(self, query: str | int) -> None:
        self.query = query
        super().__init__(f"Error: searched anime ({query}) not found")

    pass


class EntryIndexError(AppError):
    """Raised when the entry index is out of bound"""

    def __init__(self, entry_index: int, anime_title: str) -> None:
        self.entry_index = entry_index
        self.anime_title = anime_title
        super().__init__(
            f"Error: out of bound entry index: {entry_index}, for title: {anime_title}"
        )

    pass


class FileHandlerError(AppError):
    """Raised when there is file handler related error"""

    pass


class FileNotExistError(FileHandlerError):
    """Raised when the file does not exist"""

    pass


class FileEmptyError(FileHandlerError):
    """Raised when the file contains empty data"""

    pass


class MissingHeaderError(FileHandlerError):
    """Raised when the file contains data that is missing some header"""

    pass


class InvalidHeaderError(FileHandlerError):
    """Raised when the file contains data with invalid or unexpected header"""

    pass
