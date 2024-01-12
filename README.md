# API Anime Rank

## Api de controle para o projeto Anime Rank

## Endpoints API

### GET '/' 
#### Listagem top 100 animes
#### Response:
````json
    {
        "clasificacion": "1",
        "titulo_anime": "Sousou no Frieren",
        "info_anime": "TV (28 eps)\\n        Sep 2023 - \\n        451,791 members",
        "puntuacion_anime": "9.14",
        "href": "https://myanimelist.net/anime/52991/Sousou_no_Frieren",
        "Synonyms:": "Frieren at the Funeral",
        "Japanese:": "葬送のフリーレン",
        "English:": "Frieren: Beyond Journeys End",
        "Type:": "TV",
        "Episodes:": "28",
        "Status:": "Currently Airing",
        "Aired:": "Sep 29. 2023 to ?",
        "Premiered:": "Fall 2023",
        "Broadcast:": "Fridays at 23:00 (JST)",
        "Producers:": "Aniplex . Dentsu . Shogakukan-Shueisha Productions . Nippon Television Network . TOHO animation . Shogakukan",
        "Licensors:": "None found. add some",
        "Studios:": "Madhouse",
        "Source:": "Manga",
        "Genres:": "Adventure Adventure . Drama Drama . Fantasy Fantasy",
        "Demographic:": "Shounen Shounen",
        "Duration:": "24 min. per ep.",
        "Rating:": "PG-13 - Teens 13 or older",
        "Score:": "9.14 1 (scored by 137132 137.132 users) 1 indicates a weighted score .",
        "Ranked:": "#1 2 2 based on the top anime page. Please note that Not yet aired and R18+ titles are excluded.",
        "Popularity:": "#484",
        "Members:": "451.805",
        "Favorites:": "13.595"
    },
    {
    "clasificacion": "2",
    "titulo_anime": "Fullmetal Alchemist: Brotherhood",
    "info_anime": "TV (64 eps)\\n        Apr 2009 - Jul 2010\\n        3,282,538 members",
    "puntuacion_anime": "9.09",
    "href": "https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood",
    "Synonyms:": "Hagane no Renkinjutsushi: Fullmetal Alchemist. Fullmetal Alchemist (2009). FMA. FMAB",
    "Japanese:": "鋼の錬金術師 FULLMETAL ALCHEMIST",
    "English:": "Fullmetal Alchemist: Brotherhood",
    "Type:": "TV",
    "Episodes:": "64",
    "Status:": "Finished Airing",
    "Aired:": "Apr 5. 2009 to Jul 4. 2010",
    "Premiered:": "Spring 2009",
    "Broadcast:": "Sundays at 17:00 (JST)",
    "Producers:": "Aniplex . Square Enix . Mainichi Broadcasting System . Studio Moriken",
    "Licensors:": "Funimation . Aniplex of America",
    "Studios:": "Bones",
    "Source:": "Manga",
    "Genres:": "Action Action . Adventure Adventure . Drama Drama . Fantasy Fantasy",
    "Demographic:": "Shounen Shounen",
    "Duration:": "24 min. per ep.",
    "Rating:": "R - 17+ (violence & profanity)",
    "Score:": "9.09 1 (scored by 2083114 2.083.114 users) 1 indicates a weighted score .",
    "Ranked:": "#2 2 2 based on the top anime page. Please note that Not yet aired and R18+ titles are excluded.",
    "Popularity:": "#3",
    "Members:": "3.282.494",
    "Favorites:": "222.838"
    }
````

### GET '/user' 
#### Recuperar informações do usuário
#### Auth: JWT Bearer
#### Response:
````json
    {
        "username": "username",
        "email": "email",
        "user_id": 999,
        "nome": "nome",
        "sobre": "sobre",
        "img": "img"
    }
````

### POST '/query' 
#### Buscar anime pelo nome
#### Body:
````json
    {
      "query": "nome_anime"
    }
````
#### Response:
````json
    {
      "clasificacion": "2",
      "titulo_anime": "Fullmetal Alchemist: Brotherhood",
      "info_anime": "TV (64 eps)\\n        Apr 2009 - Jul 2010\\n        3,282,538 members",
      "puntuacion_anime": "9.09",
      "href": "https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood",
      "Synonyms:": "Hagane no Renkinjutsushi: Fullmetal Alchemist. Fullmetal Alchemist (2009). FMA. FMAB",
      "Japanese:": "鋼の錬金術師 FULLMETAL ALCHEMIST",
      "English:": "Fullmetal Alchemist: Brotherhood",
      "Type:": "TV",
      "Episodes:": "64",
      "Status:": "Finished Airing",
      "Aired:": "Apr 5. 2009 to Jul 4. 2010",
      "Premiered:": "Spring 2009",
      "Broadcast:": "Sundays at 17:00 (JST)",
      "Producers:": "Aniplex . Square Enix . Mainichi Broadcasting System . Studio Moriken",
      "Licensors:": "Funimation . Aniplex of America",
      "Studios:": "Bones",
      "Source:": "Manga",
      "Genres:": "Action Action . Adventure Adventure . Drama Drama . Fantasy Fantasy",
      "Demographic:": "Shounen Shounen",
      "Duration:": "24 min. per ep.",
      "Rating:": "R - 17+ (violence & profanity)",
      "Score:": "9.09 1 (scored by 2083114 2.083.114 users) 1 indicates a weighted score .",
      "Ranked:": "#2 2 2 based on the top anime page. Please note that Not yet aired and R18+ titles are excluded.",
      "Popularity:": "#3",
      "Members:": "3.282.494",
      "Favorites:": "222.838"
    }
````

### POST '/create' 
#### Criação de um novo usuário
#### Body:
````json
    {
      "username": "username",
      "email": "email",
      "password": "password"
    }
````
#### Response:
````json
    999
````

### POST '/login' 
#### Criação de um novo usuário
#### Body:
````json
    {
      "username": "username",
      "email": "email",
      "password": "password"
    }
````
#### Response:
````json
    {
      "access_token": "token",
      "token_type": "bearer",
      "user": "999"
    }
````

## Dependências do Projeto

- [annotated-types](https://pypi.org/project/annotated-types/) == 0.6.0
- [anyio](https://pypi.org/project/anyio/) == 4.2.0
- [click](https://pypi.org/project/click/) == 8.1.7
- [colorama](https://pypi.org/project/colorama/) == 0.4.6
- [ecdsa](https://pypi.org/project/ecdsa/) == 0.18.0
- [fastapi](https://pypi.org/project/fastapi/) == 0.109.0
- [h11](https://pypi.org/project/h11/) == 0.14.0
- [idna](https://pypi.org/project/idna/) == 3.6
- [pip](https://pypi.org/project/pip/) == 23.3.2
- [psycopg2](https://pypi.org/project/psycopg2/) == 2.9.9
- [pyasn1](https://pypi.org/project/pyasn1/) == 0.5.1
- [pydantic](https://pypi.org/project/pydantic/) == 2.5.3
- [pydantic-core](https://pypi.org/project/pydantic-core/) == 2.14.6
- [python-dotenv](https://pypi.org/project/python-dotenv/) == 1.0.0
- [python-jose](https://pypi.org/project/python-jose/) == 3.3.0
- [python-multipart](https://pypi.org/project/python-multipart/) == 0.0.6
- [rsa](https://pypi.org/project/rsa/) == 4.9
- [setuptools](https://pypi.org/project/setuptools/) == 69.0.3
- [six](https://pypi.org/project/six/) == 1.16.0
- [sniffio](https://pypi.org/project/sniffio/) == 1.3.0
- [starlette](https://pypi.org/project/starlette/) == 0.35.1
- [typing-extensions](https://pypi.org/project/typing-extensions/) == 4.9.0
- [uvicorn](https://pypi.org/project/uvicorn/) == 0.25.0
- [wheel](https://pypi.org/project/wheel/) == 0.42.0

