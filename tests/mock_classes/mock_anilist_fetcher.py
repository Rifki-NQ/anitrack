from typing import Any


class MockAnilistFetcherNormal:
    async def fetch_data_by_title(
        self, anime_title: str = "Attack on titan", sort: str = "relevance"
    ) -> list[dict[str, Any]]:
        return [
            {
                "averageScore": 85,
                "duration": 24,
                "endDate": {"day": 28, "month": 9, "year": 2013},
                "episodes": 25,
                "format": "TV",
                "genres": ["Action", "Drama", "Fantasy", "Mystery"],
                "id": 16498,
                "rankings": [
                    {"allTime": True, "rank": 67, "type": "RATED"},
                    {"allTime": True, "rank": 1, "type": "POPULAR"},
                    {"allTime": False, "rank": 2, "type": "RATED"},
                    {"allTime": False, "rank": 1, "type": "POPULAR"},
                    {"allTime": False, "rank": 1, "type": "RATED"},
                    {"allTime": False, "rank": 1, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 7, "month": 4, "year": 2013},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "WIT STUDIO"},
                        {"isAnimationStudio": False, "name": "Pony Canyon"},
                        {"isAnimationStudio": False, "name": "Kodansha"},
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {"isAnimationStudio": False, "name": "Dentsu"},
                        {"isAnimationStudio": False, "name": "Pony Canyon Enterprise"},
                        {
                            "isAnimationStudio": False,
                            "name": "Mainichi Broadcasting System",
                        },
                    ]
                },
                "title": {"english": "Attack on Titan", "romaji": "Shingeki no Kyojin"},
            },
            {
                "averageScore": 87,
                "duration": 24,
                "endDate": {"day": 29, "month": 3, "year": 2021},
                "episodes": 16,
                "format": "TV",
                "genres": ["Action", "Drama", "Fantasy", "Mystery"],
                "id": 110277,
                "rankings": [
                    {"allTime": True, "rank": 34, "type": "RATED"},
                    {"allTime": True, "rank": 16, "type": "POPULAR"},
                    {"allTime": False, "rank": 1, "type": "RATED"},
                    {"allTime": False, "rank": 2, "type": "POPULAR"},
                    {"allTime": False, "rank": 1, "type": "RATED"},
                    {"allTime": False, "rank": 1, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 7, "month": 12, "year": 2020},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "MAPPA"},
                        {"isAnimationStudio": False, "name": "Pony Canyon"},
                        {"isAnimationStudio": False, "name": "Kodansha"},
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {"isAnimationStudio": False, "name": "Dentsu"},
                        {
                            "isAnimationStudio": False,
                            "name": "Mainichi Broadcasting System",
                        },
                        {"isAnimationStudio": False, "name": "Pony Canyon Enterprise"},
                        {"isAnimationStudio": True, "name": "MAPPA"},
                    ]
                },
                "title": {
                    "english": "Attack on Titan Final Season",
                    "romaji": "Shingeki no Kyojin: The Final Season",
                },
            },
            {
                "averageScore": 77,
                "duration": 25,
                "endDate": {"day": 8, "month": 8, "year": 2014},
                "episodes": 3,
                "format": "OVA",
                "genres": ["Action", "Drama", "Fantasy", "Mystery"],
                "id": 18397,
                "rankings": [
                    {"allTime": True, "rank": 64, "type": "RATED"},
                    {"allTime": True, "rank": 4, "type": "POPULAR"},
                    {"allTime": False, "rank": 3, "type": "RATED"},
                    {"allTime": False, "rank": 1, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 9, "month": 12, "year": 2013},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "WIT STUDIO"},
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {
                            "isAnimationStudio": False,
                            "name": "Mainichi Broadcasting System",
                        },
                        {"isAnimationStudio": False, "name": "Pony Canyon"},
                        {"isAnimationStudio": False, "name": "Kodansha"},
                        {"isAnimationStudio": False, "name": "Shingeki no Kyojin Team"},
                    ]
                },
                "title": {
                    "english": "Attack on Titan OVA",
                    "romaji": "Shingeki no Kyojin OVA",
                },
            },
            {
                "averageScore": 85,
                "duration": 25,
                "endDate": {"day": 17, "month": 6, "year": 2017},
                "episodes": 12,
                "format": "TV",
                "genres": ["Action", "Drama", "Fantasy", "Mystery"],
                "id": 20958,
                "rankings": [
                    {"allTime": True, "rank": 79, "type": "RATED"},
                    {"allTime": True, "rank": 10, "type": "POPULAR"},
                    {"allTime": False, "rank": 6, "type": "RATED"},
                    {"allTime": False, "rank": 1, "type": "POPULAR"},
                    {"allTime": False, "rank": 2, "type": "RATED"},
                    {"allTime": False, "rank": 1, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 1, "month": 4, "year": 2017},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "WIT STUDIO"},
                        {"isAnimationStudio": False, "name": "Pony Canyon"},
                        {"isAnimationStudio": False, "name": "Kodansha"},
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {"isAnimationStudio": False, "name": "Dentsu"},
                        {"isAnimationStudio": False, "name": "Pony Canyon Enterprise"},
                        {
                            "isAnimationStudio": False,
                            "name": "Mainichi Broadcasting System",
                        },
                        {"isAnimationStudio": False, "name": "Funimation"},
                    ]
                },
                "title": {
                    "english": "Attack on Titan Season 2",
                    "romaji": "Shingeki no Kyojin Season 2",
                },
            },
            {
                "averageScore": 86,
                "duration": 24,
                "endDate": {"day": 15, "month": 10, "year": 2018},
                "episodes": 12,
                "format": "TV",
                "genres": ["Action", "Drama", "Fantasy", "Mystery"],
                "id": 99147,
                "rankings": [
                    {"allTime": True, "rank": 56, "type": "RATED"},
                    {"allTime": True, "rank": 14, "type": "POPULAR"},
                    {"allTime": False, "rank": 3, "type": "RATED"},
                    {"allTime": False, "rank": 1, "type": "POPULAR"},
                    {"allTime": False, "rank": 2, "type": "RATED"},
                    {"allTime": False, "rank": 1, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 23, "month": 7, "year": 2018},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "WIT STUDIO"},
                        {"isAnimationStudio": False, "name": "Pony Canyon"},
                        {"isAnimationStudio": False, "name": "Kodansha"},
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {"isAnimationStudio": False, "name": "Dentsu"},
                        {"isAnimationStudio": False, "name": "Pony Canyon Enterprise"},
                        {
                            "isAnimationStudio": False,
                            "name": "Mainichi Broadcasting System",
                        },
                    ]
                },
                "title": {
                    "english": "Attack on Titan Season 3",
                    "romaji": "Shingeki no Kyojin Season 3",
                },
            },
            {
                "averageScore": 83,
                "duration": 28,
                "endDate": {"day": 9, "month": 4, "year": 2015},
                "episodes": 2,
                "format": "OVA",
                "genres": ["Action", "Drama", "Fantasy"],
                "id": 20811,
                "rankings": [
                    {"allTime": True, "rank": 5, "type": "RATED"},
                    {"allTime": True, "rank": 3, "type": "POPULAR"},
                    {"allTime": False, "rank": 1, "type": "RATED"},
                    {"allTime": False, "rank": 1, "type": "POPULAR"},
                ],
                "source": "VISUAL_NOVEL",
                "startDate": {"day": 9, "month": 12, "year": 2014},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {"isAnimationStudio": True, "name": "WIT STUDIO"},
                    ]
                },
                "title": {
                    "english": "Attack on Titan: No Regrets",
                    "romaji": "Shingeki no Kyojin Gaiden: Kuinaki Sentaku",
                },
            },
            {
                "averageScore": 77,
                "duration": 120,
                "endDate": {"day": 17, "month": 7, "year": 2020},
                "episodes": 1,
                "format": "MOVIE",
                "genres": ["Action", "Drama", "Fantasy", "Mystery"],
                "id": 119113,
                "rankings": [
                    {"allTime": True, "rank": 221, "type": "RATED"},
                    {"allTime": True, "rank": 233, "type": "POPULAR"},
                    {"allTime": False, "rank": 10, "type": "RATED"},
                    {"allTime": False, "rank": 11, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 17, "month": 7, "year": 2020},
                "status": "FINISHED",
                "studios": {
                    "nodes": [{"isAnimationStudio": True, "name": "WIT STUDIO"}]
                },
                "title": {
                    "english": "Attack on Titan ~Chronicle~",
                    "romaji": "Shingeki no Kyojin: Chronicle",
                },
            },
            {
                "averageScore": 63,
                "duration": 11,
                "endDate": {"day": 19, "month": 3, "year": 2014},
                "episodes": 9,
                "format": "SPECIAL",
                "genres": ["Action", "Comedy", "Drama", "Fantasy"],
                "id": 19391,
                "rankings": [],
                "source": "MANGA",
                "startDate": {"day": 17, "month": 7, "year": 2013},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {"isAnimationStudio": True, "name": "WIT STUDIO"},
                    ]
                },
                "title": {
                    "english": "Attack on Titan Picture Drama",
                    "romaji": "Shingeki no Kyojin: Chimi Kyara Gekijou - Tondeke! "
                    "Kunren Heidan",
                },
            },
            {
                "averageScore": 77,
                "duration": 25,
                "endDate": {"day": 9, "month": 8, "year": 2018},
                "episodes": 3,
                "format": "OVA",
                "genres": ["Action", "Drama", "Fantasy", "Mystery"],
                "id": 99634,
                "rankings": [
                    {"allTime": True, "rank": 63, "type": "RATED"},
                    {"allTime": True, "rank": 13, "type": "POPULAR"},
                    {"allTime": False, "rank": 2, "type": "RATED"},
                    {"allTime": False, "rank": 2, "type": "POPULAR"},
                ],
                "source": "LIGHT_NOVEL",
                "startDate": {"day": 8, "month": 12, "year": 2017},
                "status": "FINISHED",
                "studios": {
                    "nodes": [{"isAnimationStudio": True, "name": "WIT STUDIO"}]
                },
                "title": {
                    "english": "Attack on Titan: Lost Girls",
                    "romaji": "Shingeki no Kyojin: LOST GIRLS",
                },
            },
            {
                "averageScore": 70,
                "duration": 18,
                "endDate": {"day": 20, "month": 12, "year": 2015},
                "episodes": 12,
                "format": "TV",
                "genres": ["Comedy", "Fantasy", "Slice of Life"],
                "id": 21281,
                "rankings": [
                    {"allTime": False, "rank": 65, "type": "RATED"},
                    {"allTime": False, "rank": 49, "type": "POPULAR"},
                    {"allTime": False, "rank": 18, "type": "RATED"},
                    {"allTime": False, "rank": 10, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 4, "month": 10, "year": 2015},
                "status": "FINISHED",
                "studios": {
                    "nodes": [{"isAnimationStudio": True, "name": "Production I.G"}]
                },
                "title": {
                    "english": "Attack on Titan: Junior High",
                    "romaji": "Shingeki! Kyojin Chuugakkou",
                },
            },
            {
                "averageScore": 77,
                "duration": 120,
                "endDate": {"day": 13, "month": 1, "year": 2018},
                "episodes": 1,
                "format": "MOVIE",
                "genres": ["Action", "Drama", "Fantasy", "Mystery"],
                "id": 100465,
                "rankings": [
                    {"allTime": True, "rank": 207, "type": "RATED"},
                    {"allTime": False, "rank": 10, "type": "RATED"},
                    {"allTime": False, "rank": 15, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 13, "month": 1, "year": 2018},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "WIT STUDIO"},
                        {"isAnimationStudio": False, "name": "Shingeki no Kyojin Team"},
                        {"isAnimationStudio": False, "name": "Funimation"},
                        {"isAnimationStudio": False, "name": "Madman Entertainment"},
                        {"isAnimationStudio": False, "name": "Selecta Visión"},
                    ]
                },
                "title": {
                    "english": "Attack on Titan: The Roar of Awakening",
                    "romaji": "Shingeki no Kyojin Season 2: Kakusei no Houkou",
                },
            },
            {
                "averageScore": 77,
                "duration": 5,
                "endDate": {"day": 4, "month": 8, "year": 2021},
                "episodes": 2,
                "format": "SPECIAL",
                "genres": ["Comedy", "Fantasy"],
                "id": 139754,
                "rankings": [],
                "source": "MANGA",
                "startDate": {"day": 7, "month": 7, "year": 2021},
                "status": "FINISHED",
                "studios": {"nodes": [{"isAnimationStudio": True, "name": "MAPPA"}]},
                "title": {
                    "english": "Attack On Titan: The Final Season Specials",
                    "romaji": "Shingeki no Kyojin: Chimi Kyara Gekijou - Final",
                },
            },
            {
                "averageScore": 86,
                "duration": 24,
                "endDate": {"day": 4, "month": 4, "year": 2022},
                "episodes": 12,
                "format": "TV",
                "genres": ["Action", "Drama", "Fantasy", "Mystery", "Psychological"],
                "id": 131681,
                "rankings": [
                    {"allTime": True, "rank": 40, "type": "RATED"},
                    {"allTime": True, "rank": 69, "type": "POPULAR"},
                    {"allTime": False, "rank": 5, "type": "RATED"},
                    {"allTime": False, "rank": 3, "type": "POPULAR"},
                    {"allTime": False, "rank": 1, "type": "RATED"},
                    {"allTime": False, "rank": 2, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 10, "month": 1, "year": 2022},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "MAPPA"},
                        {"isAnimationStudio": False, "name": "Pony Canyon"},
                        {"isAnimationStudio": False, "name": "Kodansha"},
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {"isAnimationStudio": False, "name": "Dentsu"},
                        {
                            "isAnimationStudio": False,
                            "name": "Mainichi Broadcasting System",
                        },
                        {"isAnimationStudio": False, "name": "Pony Canyon Enterprise"},
                        {"isAnimationStudio": True, "name": "MAPPA"},
                    ]
                },
                "title": {
                    "english": "Attack on Titan Final Season Part 2",
                    "romaji": "Shingeki no Kyojin: The Final Season Part 2",
                },
            },
            {
                "averageScore": 76,
                "duration": 120,
                "endDate": {"day": 27, "month": 6, "year": 2015},
                "episodes": 1,
                "format": "MOVIE",
                "genres": ["Action", "Drama", "Fantasy"],
                "id": 20692,
                "rankings": [
                    {"allTime": True, "rank": 242, "type": "RATED"},
                    {"allTime": True, "rank": 261, "type": "POPULAR"},
                    {"allTime": False, "rank": 11, "type": "RATED"},
                    {"allTime": False, "rank": 13, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 27, "month": 6, "year": 2015},
                "status": "FINISHED",
                "studios": {
                    "nodes": [{"isAnimationStudio": True, "name": "WIT STUDIO"}]
                },
                "title": {
                    "english": "Attack on Titan Part II: Wings of Freedom",
                    "romaji": "Shingeki no Kyojin Kouhen: Jiyuu no Tsubasa",
                },
            },
            {
                "averageScore": 90,
                "duration": 24,
                "endDate": {"day": 1, "month": 7, "year": 2019},
                "episodes": 10,
                "format": "TV",
                "genres": ["Action", "Drama", "Fantasy", "Mystery"],
                "id": 104578,
                "rankings": [
                    {"allTime": True, "rank": 4, "type": "RATED"},
                    {"allTime": True, "rank": 22, "type": "POPULAR"},
                    {"allTime": False, "rank": 1, "type": "RATED"},
                    {"allTime": False, "rank": 3, "type": "POPULAR"},
                    {"allTime": False, "rank": 1, "type": "RATED"},
                    {"allTime": False, "rank": 2, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 29, "month": 4, "year": 2019},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "WIT STUDIO"},
                        {"isAnimationStudio": False, "name": "Pony Canyon"},
                        {"isAnimationStudio": False, "name": "Kodansha"},
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {"isAnimationStudio": False, "name": "Dentsu"},
                        {"isAnimationStudio": False, "name": "Pony Canyon Enterprise"},
                        {
                            "isAnimationStudio": False,
                            "name": "Mainichi Broadcasting System",
                        },
                    ]
                },
                "title": {
                    "english": "Attack on Titan Season 3 Part 2",
                    "romaji": "Shingeki no Kyojin Season 3 Part 2",
                },
            },
            {
                "averageScore": 75,
                "duration": 2,
                "endDate": {"day": 27, "month": 2, "year": 2019},
                "episodes": 4,
                "format": "SPECIAL",
                "genres": ["Comedy", "Fantasy"],
                "id": 108942,
                "rankings": [],
                "source": "MANGA",
                "startDate": {"day": 17, "month": 10, "year": 2018},
                "status": "FINISHED",
                "studios": {
                    "nodes": [{"isAnimationStudio": True, "name": "WIT STUDIO"}]
                },
                "title": {
                    "english": None,
                    "romaji": "Shingeki no Kyojin: Chimi Kyara Gekijou - Rivai-han",
                },
            },
            {
                "averageScore": 87,
                "duration": 85,
                "endDate": {"day": 5, "month": 11, "year": 2023},
                "episodes": 1,
                "format": "SPECIAL",
                "genres": ["Action", "Drama", "Fantasy", "Psychological", "Romance"],
                "id": 162314,
                "rankings": [],
                "source": "MANGA",
                "startDate": {"day": 5, "month": 11, "year": 2023},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "MAPPA"},
                        {"isAnimationStudio": False, "name": "Pony Canyon"},
                        {"isAnimationStudio": False, "name": "Kodansha"},
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {"isAnimationStudio": False, "name": "Dentsu"},
                        {
                            "isAnimationStudio": False,
                            "name": "Mainichi Broadcasting System",
                        },
                        {"isAnimationStudio": False, "name": "qooop"},
                        {"isAnimationStudio": True, "name": "MAPPA"},
                    ]
                },
                "title": {
                    "english": "Attack on Titan Final Season THE FINAL CHAPTERS "
                    "Special 2",
                    "romaji": "Shingeki no Kyojin: The Final Season - Kanketsu-hen "
                    "Kouhen",
                },
            },
            {
                "averageScore": 79,
                "duration": 2,
                "endDate": {"day": 18, "month": 9, "year": 2019},
                "episodes": 3,
                "format": "SPECIAL",
                "genres": ["Comedy", "Fantasy"],
                "id": 120257,
                "rankings": [],
                "source": "MANGA",
                "startDate": {"day": 24, "month": 7, "year": 2019},
                "status": "FINISHED",
                "studios": {
                    "nodes": [{"isAnimationStudio": True, "name": "WIT STUDIO"}]
                },
                "title": {
                    "english": None,
                    "romaji": "Shingeki no Kyojin: Chimi Kyara Gekijou - Rivai-han "
                    "Part 2",
                },
            },
            {
                "averageScore": 87,
                "duration": 61,
                "endDate": {"day": 4, "month": 3, "year": 2023},
                "episodes": 1,
                "format": "SPECIAL",
                "genres": ["Action", "Drama", "Fantasy", "Mystery", "Psychological"],
                "id": 146984,
                "rankings": [],
                "source": "MANGA",
                "startDate": {"day": 4, "month": 3, "year": 2023},
                "status": "FINISHED",
                "studios": {
                    "nodes": [
                        {"isAnimationStudio": True, "name": "MAPPA"},
                        {"isAnimationStudio": False, "name": "Pony Canyon"},
                        {"isAnimationStudio": False, "name": "Kodansha"},
                        {"isAnimationStudio": True, "name": "Production I.G"},
                        {"isAnimationStudio": False, "name": "Dentsu"},
                        {
                            "isAnimationStudio": False,
                            "name": "Mainichi Broadcasting System",
                        },
                        {"isAnimationStudio": False, "name": "qooop"},
                        {"isAnimationStudio": True, "name": "MAPPA"},
                    ]
                },
                "title": {
                    "english": "Attack on Titan Final Season THE FINAL CHAPTERS "
                    "Special 1",
                    "romaji": "Shingeki no Kyojin: The Final Season - Kanketsu-hen "
                    "Zenpen",
                },
            },
            {
                "averageScore": 75,
                "duration": 118,
                "endDate": {"day": 22, "month": 11, "year": 2014},
                "episodes": 1,
                "format": "MOVIE",
                "genres": ["Action", "Drama", "Fantasy"],
                "id": 20691,
                "rankings": [
                    {"allTime": True, "rank": 273, "type": "POPULAR"},
                    {"allTime": False, "rank": 8, "type": "RATED"},
                    {"allTime": False, "rank": 5, "type": "POPULAR"},
                ],
                "source": "MANGA",
                "startDate": {"day": 22, "month": 11, "year": 2014},
                "status": "FINISHED",
                "studios": {
                    "nodes": [{"isAnimationStudio": True, "name": "WIT STUDIO"}]
                },
                "title": {
                    "english": "Attack on Titan Part I: Crimson Bow and Arrow",
                    "romaji": "Shingeki no Kyojin Zenpen: Guren no Yumiya",
                },
            },
        ]

    async def fetch_data_by_id(self, anime_id: int = 16498) -> dict[str, Any]:
        return {
            "averageScore": 85,
            "duration": 24,
            "endDate": {"day": 28, "month": 9, "year": 2013},
            "episodes": 25,
            "format": "TV",
            "genres": ["Action", "Drama", "Fantasy", "Mystery"],
            "id": 16498,
            "rankings": [
                {"allTime": True, "rank": 67, "type": "RATED"},
                {"allTime": True, "rank": 1, "type": "POPULAR"},
                {"allTime": False, "rank": 2, "type": "RATED"},
                {"allTime": False, "rank": 1, "type": "POPULAR"},
                {"allTime": False, "rank": 1, "type": "RATED"},
                {"allTime": False, "rank": 1, "type": "POPULAR"},
            ],
            "source": "MANGA",
            "startDate": {"day": 7, "month": 4, "year": 2013},
            "status": "FINISHED",
            "studios": {
                "nodes": [
                    {"isAnimationStudio": True, "name": "WIT STUDIO"},
                    {"isAnimationStudio": False, "name": "Pony Canyon"},
                    {"isAnimationStudio": False, "name": "Kodansha"},
                    {"isAnimationStudio": True, "name": "Production I.G"},
                    {"isAnimationStudio": False, "name": "Dentsu"},
                    {"isAnimationStudio": False, "name": "Pony Canyon Enterprise"},
                    {
                        "isAnimationStudio": False,
                        "name": "Mainichi Broadcasting System",
                    },
                ]
            },
            "title": {"english": "Attack on Titan", "romaji": "Shingeki no Kyojin"},
        }
