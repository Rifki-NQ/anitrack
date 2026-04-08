from typing import Any

class MockJikanFetcher:
    def fetch_data_by_title(self, anime_title: str = "Attack on titan", entry_number: int = 0) -> dict[str, Any]:
        return {'aired': {'from': '2013-04-07T00:00:00+00:00',
                'prop': {'from': {'day': 7, 'month': 4, 'year': 2013},
                            'to': {'day': 29, 'month': 9, 'year': 2013}},
                'string': 'Apr 7, 2013 to Sep 29, 2013',
                'to': '2013-09-29T00:00:00+00:00'},
        'airing': False,
        'approved': True,
        'background': 'Shingeki no Kyojin adapts content from the first eight volumes '
                    "of Hajime Isayama's award-winning manga of the same name. The "
                    'anime won the Animation of the Year in the Television category '
                    'at the Tokyo Anime Award Festival in 2014.',
        'broadcast': {'day': 'Sundays',
                    'string': 'Sundays at 01:58 (JST)',
                    'time': '01:58',
                    'timezone': 'Asia/Tokyo'},
        'demographics': [{'mal_id': 27,
                        'name': 'Shounen',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/27/Shounen'}],
        'duration': '24 min per ep',
        'episodes': 25,
        'explicit_genres': [],
        'favorites': 188134,
        'genres': [{'mal_id': 1,
                    'name': 'Action',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/1/Action'},
                    {'mal_id': 46,
                    'name': 'Award Winning',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/46/Award_Winning'},
                    {'mal_id': 8,
                    'name': 'Drama',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/8/Drama'},
                    {'mal_id': 41,
                    'name': 'Suspense',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/41/Suspense'}],
        'images': {'jpg': {'image_url': 'https://myanimelist.net/images/anime/10/47347.jpg',
                            'large_image_url': 'https://myanimelist.net/images/anime/10/47347l.jpg',
                            'small_image_url': 'https://myanimelist.net/images/anime/10/47347t.jpg'},
                    'webp': {'image_url': 'https://myanimelist.net/images/anime/10/47347.webp',
                            'large_image_url': 'https://myanimelist.net/images/anime/10/47347l.webp',
                            'small_image_url': 'https://myanimelist.net/images/anime/10/47347t.webp'}},
        'licensors': [{'mal_id': 102,
                        'name': 'Funimation',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/102/Funimation'}],
        'mal_id': 16498,
        'members': 4338901,
        'popularity': 1,
        'producers': [{'mal_id': 10,
                        'name': 'Production I.G',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/10/Production_IG'},
                    {'mal_id': 53,
                        'name': 'Dentsu',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/53/Dentsu'},
                    {'mal_id': 143,
                        'name': 'Mainichi Broadcasting System',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/143/Mainichi_Broadcasting_System'},
                    {'mal_id': 144,
                        'name': 'Pony Canyon',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/144/Pony_Canyon'},
                    {'mal_id': 159,
                        'name': 'Kodansha',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/159/Kodansha'},
                    {'mal_id': 1557,
                        'name': 'Pony Canyon Enterprises',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/1557/Pony_Canyon_Enterprises'}],
        'rank': 124,
        'rating': 'R - 17+ (violence & profanity)',
        'score': 8.57,
        'scored_by': 3053718,
        'season': 'spring',
        'source': 'Manga',
        'status': 'Finished Airing',
        'studios': [{'mal_id': 858,
                    'name': 'Wit Studio',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/producer/858/Wit_Studio'}],
        'synopsis': 'Centuries ago, mankind was slaughtered to near extinction by '
                    'monstrous humanoid creatures called Titans, forcing humans to '
                    'hide in fear behind enormous concentric walls. What makes these '
                    'giants truly terrifying is that their taste for human flesh is '
                    'not born out of hunger but what appears to be out of pleasure. '
                    'To ensure their survival, the remnants of humanity began living '
                    'within defensive barriers, resulting in one hundred years '
                    'without a single titan encounter. However, that fragile calm is '
                    'soon shattered when a colossal Titan manages to breach the '
                    'supposedly impregnable outer wall, reigniting the fight for '
                    'survival against the man-eating abominations.\n'
                    '\n'
                    'After witnessing a horrific personal loss at the hands of the '
                    'invading creatures, Eren Yeager dedicates his life to their '
                    'eradication by enlisting into the Survey Corps, an elite '
                    'military unit that combats the merciless humanoids outside the '
                    'protection of the walls. Eren, his adopted sister Mikasa '
                    'Ackerman, and his childhood friend Armin Arlert join the brutal '
                    'war against the Titans and race to discover a way of defeating '
                    'them before the last walls are breached.\n'
                    '\n'
                    '[Written by MAL Rewrite]',
        'themes': [{'mal_id': 58,
                    'name': 'Gore',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/58/Gore'},
                    {'mal_id': 38,
                    'name': 'Military',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/38/Military'},
                    {'mal_id': 76,
                    'name': 'Survival',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/76/Survival'}],
        'title': 'Shingeki no Kyojin',
        'title_english': 'Attack on Titan',
        'title_japanese': '進撃の巨人',
        'title_synonyms': ['AoT', 'SnK'],
        'titles': [{'title': 'Shingeki no Kyojin', 'type': 'Default'},
                    {'title': 'AoT', 'type': 'Synonym'},
                    {'title': 'SnK', 'type': 'Synonym'},
                    {'title': '進撃の巨人', 'type': 'Japanese'},
                    {'title': 'Attack on Titan', 'type': 'English'},
                    {'title': 'Attack on Titan', 'type': 'German'},
                    {'title': 'Ataque a los Titanes', 'type': 'Spanish'},
                    {'title': "L'Attaque des Titans", 'type': 'French'}],
        'trailer': {'embed_url': 'https://www.youtube-nocookie.com/embed/LHtdKWJdif4?enablejsapi=1&wmode=opaque&autoplay=1',
                    'images': {'image_url': None,
                                'large_image_url': None,
                                'maximum_image_url': None,
                                'medium_image_url': None,
                                'small_image_url': None},
                    'url': None,
                    'youtube_id': None},
        'type': 'TV',
        'url': 'https://myanimelist.net/anime/16498/Shingeki_no_Kyojin',
        'year': 2013}

    def fetch_data_by_id(self, anime_id: int = 16498) -> dict[str, Any]:
        return {'aired': {'from': '2013-04-07T00:00:00+00:00',
                'prop': {'from': {'day': 7, 'month': 4, 'year': 2013},
                            'to': {'day': 29, 'month': 9, 'year': 2013}},
                'string': 'Apr 7, 2013 to Sep 29, 2013',
                'to': '2013-09-29T00:00:00+00:00'},
        'airing': False,
        'approved': True,
        'background': 'Shingeki no Kyojin adapts content from the first eight volumes '
                    "of Hajime Isayama's award-winning manga of the same name. The "
                    'anime won the Animation of the Year in the Television category '
                    'at the Tokyo Anime Award Festival in 2014.',
        'broadcast': {'day': 'Sundays',
                    'string': 'Sundays at 01:58 (JST)',
                    'time': '01:58',
                    'timezone': 'Asia/Tokyo'},
        'demographics': [{'mal_id': 27,
                        'name': 'Shounen',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/genre/27/Shounen'}],
        'duration': '24 min per ep',
        'episodes': 25,
        'explicit_genres': [],
        'favorites': 188134,
        'genres': [{'mal_id': 1,
                    'name': 'Action',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/1/Action'},
                    {'mal_id': 46,
                    'name': 'Award Winning',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/46/Award_Winning'},
                    {'mal_id': 8,
                    'name': 'Drama',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/8/Drama'},
                    {'mal_id': 41,
                    'name': 'Suspense',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/41/Suspense'}],
        'images': {'jpg': {'image_url': 'https://myanimelist.net/images/anime/10/47347.jpg',
                            'large_image_url': 'https://myanimelist.net/images/anime/10/47347l.jpg',
                            'small_image_url': 'https://myanimelist.net/images/anime/10/47347t.jpg'},
                    'webp': {'image_url': 'https://myanimelist.net/images/anime/10/47347.webp',
                            'large_image_url': 'https://myanimelist.net/images/anime/10/47347l.webp',
                            'small_image_url': 'https://myanimelist.net/images/anime/10/47347t.webp'}},
        'licensors': [{'mal_id': 102,
                        'name': 'Funimation',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/102/Funimation'}],
        'mal_id': 16498,
        'members': 4338901,
        'popularity': 1,
        'producers': [{'mal_id': 10,
                        'name': 'Production I.G',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/10/Production_IG'},
                    {'mal_id': 53,
                        'name': 'Dentsu',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/53/Dentsu'},
                    {'mal_id': 143,
                        'name': 'Mainichi Broadcasting System',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/143/Mainichi_Broadcasting_System'},
                    {'mal_id': 144,
                        'name': 'Pony Canyon',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/144/Pony_Canyon'},
                    {'mal_id': 159,
                        'name': 'Kodansha',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/159/Kodansha'},
                    {'mal_id': 1557,
                        'name': 'Pony Canyon Enterprises',
                        'type': 'anime',
                        'url': 'https://myanimelist.net/anime/producer/1557/Pony_Canyon_Enterprises'}],
        'rank': 124,
        'rating': 'R - 17+ (violence & profanity)',
        'score': 8.57,
        'scored_by': 3053718,
        'season': 'spring',
        'source': 'Manga',
        'status': 'Finished Airing',
        'studios': [{'mal_id': 858,
                    'name': 'Wit Studio',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/producer/858/Wit_Studio'}],
        'synopsis': 'Centuries ago, mankind was slaughtered to near extinction by '
                    'monstrous humanoid creatures called Titans, forcing humans to '
                    'hide in fear behind enormous concentric walls. What makes these '
                    'giants truly terrifying is that their taste for human flesh is '
                    'not born out of hunger but what appears to be out of pleasure. '
                    'To ensure their survival, the remnants of humanity began living '
                    'within defensive barriers, resulting in one hundred years '
                    'without a single titan encounter. However, that fragile calm is '
                    'soon shattered when a colossal Titan manages to breach the '
                    'supposedly impregnable outer wall, reigniting the fight for '
                    'survival against the man-eating abominations.\n'
                    '\n'
                    'After witnessing a horrific personal loss at the hands of the '
                    'invading creatures, Eren Yeager dedicates his life to their '
                    'eradication by enlisting into the Survey Corps, an elite '
                    'military unit that combats the merciless humanoids outside the '
                    'protection of the walls. Eren, his adopted sister Mikasa '
                    'Ackerman, and his childhood friend Armin Arlert join the brutal '
                    'war against the Titans and race to discover a way of defeating '
                    'them before the last walls are breached.\n'
                    '\n'
                    '[Written by MAL Rewrite]',
        'themes': [{'mal_id': 58,
                    'name': 'Gore',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/58/Gore'},
                    {'mal_id': 38,
                    'name': 'Military',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/38/Military'},
                    {'mal_id': 76,
                    'name': 'Survival',
                    'type': 'anime',
                    'url': 'https://myanimelist.net/anime/genre/76/Survival'}],
        'title': 'Shingeki no Kyojin',
        'title_english': 'Attack on Titan',
        'title_japanese': '進撃の巨人',
        'title_synonyms': ['AoT', 'SnK'],
        'titles': [{'title': 'Shingeki no Kyojin', 'type': 'Default'},
                    {'title': 'AoT', 'type': 'Synonym'},
                    {'title': 'SnK', 'type': 'Synonym'},
                    {'title': '進撃の巨人', 'type': 'Japanese'},
                    {'title': 'Attack on Titan', 'type': 'English'},
                    {'title': 'Attack on Titan', 'type': 'German'},
                    {'title': 'Ataque a los Titanes', 'type': 'Spanish'},
                    {'title': "L'Attaque des Titans", 'type': 'French'}],
        'trailer': {'embed_url': 'https://www.youtube-nocookie.com/embed/LHtdKWJdif4?enablejsapi=1&wmode=opaque&autoplay=1',
                    'images': {'image_url': None,
                                'large_image_url': None,
                                'maximum_image_url': None,
                                'medium_image_url': None,
                                'small_image_url': None},
                    'url': None,
                    'youtube_id': None},
        'type': 'TV',
        'url': 'https://myanimelist.net/anime/16498/Shingeki_no_Kyojin',
        'year': 2013}
        
class MockAnilistFetcher:
    def fetch_data_by_title(self, anime_title: str = "Attack on titan", entry_number: int = 0) -> dict[str, Any]:
        return {'averageScore': 85,
                'episodes': 25,
                'genres': ['Action', 'Drama', 'Fantasy', 'Mystery'],
                'id': 16498,
                'title': {'english': 'Attack on Titan', 'romaji': 'Shingeki no Kyojin'}}
    
    def fetch_data_by_id(self, anime_id: int = 16498) -> dict[str, Any]:
        return {'averageScore': 85,
                'episodes': 25,
                'genres': ['Action', 'Drama', 'Fantasy', 'Mystery'],
                'id': 16498,
                'title': {'english': 'Attack on Titan', 'romaji': 'Shingeki no Kyojin'}}