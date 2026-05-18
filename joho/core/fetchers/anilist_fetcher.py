import httpx
from typing import Any, cast
from joho.core.fetchers.base_fetcher import FetchData
from joho.core.exceptions import AnilistError, AppConnectionError
from joho.core.constants import GLOBAL_TIMEOUT


class FetchAnilist(FetchData):
    def __init__(self, client: httpx.AsyncClient) -> None:
        super().__init__(client)

    BASE_URL = "https://graphql.anilist.co"
    SORT_MAP = {
        "rating": "SCORE_DESC",
        "popularity": "POPULARITY_DESC",
        "relevance": "SEARCH_MATCH",
        "newest": "START_DATE_DESC",
        "oldest": "START_DATE",
    }
    QUERY_BY_TITLE = """
    query ($search: String, $sort: [MediaSort]) {
        Page (page: 1, perPage: 50) {
            media (search: $search, sort: $sort, type: ANIME) {
                id
                title {
                    romaji
                    english
                }
                format
                status
                startDate {
                    year
                    month
                    day
                }
                endDate {
                    year
                    month
                    day
                }
                episodes
                duration
                genres
                source
                averageScore
                studios {
                    nodes {
                        name
                        isAnimationStudio
                    }
                }
                rankings {
                    rank
                    type
                    allTime
                }
            }
        }
    }
    """
    QUERY_BY_ID = """
    query ($id: Int) {
        Media (id: $id, type: ANIME) {
            id
            title {
                romaji
                english
            }
            format
            status
            startDate {
                year
                month
                day
            }
            endDate {
                year
                month
                day
            }
            episodes
            duration
            genres
            source
            averageScore
            studios {
                nodes {
                    name
                    isAnimationStudio
                }
            }
            rankings {
                rank
                type
                allTime
            }
        }
    }
    """

    async def fetch_data_by_title(
        self, anime_title: str, sort: str
    ) -> list[dict[str, Any]]:
        data = await self._request(
            url=self.BASE_URL,
            query=self.QUERY_BY_TITLE,
            variables={"search": anime_title, "sort": [self.SORT_MAP[sort]]},
        )
        media_data = data.json()["data"]["Page"]["media"]
        if not media_data:
            raise AnilistError("Error: requested anime not found!")
        return cast(list[dict[str, Any]], media_data)

    async def fetch_data_by_id(self, anime_id: int) -> dict[str, Any]:
        data = await self._request(
            url=self.BASE_URL, query=self.QUERY_BY_ID, variables={"id": anime_id}
        )
        media_data = data.json()["data"]["Media"]
        if not media_data:
            raise AnilistError("Error: requested anime not found!")
        return cast(dict[str, Any], media_data)

    async def _request(
        self, url: str, query: str, variables: dict[str, str | int | list[str]]
    ) -> httpx.Response:
        try:
            response = await self.client.post(
                url,
                json={"query": query, "variables": variables},
                timeout=GLOBAL_TIMEOUT,
            )
            response.raise_for_status()
            return response
        except httpx.RequestError as e:
            raise AppConnectionError(f"Connection error occurred: {e}") from e
        except httpx.HTTPStatusError as e:
            raise AppConnectionError(f"API returned: {e.response.status_code}") from e
