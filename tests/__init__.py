from core.fetcher import FetchData
anilist_handler = FetchData.create_fetcher("anilist")

def test_anilist_fetcher():
    print(anilist_handler.fetch_data())