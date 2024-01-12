import os
import psycopg2
from dotenv import load_dotenv

def lista() -> list[dict]:
    load_dotenv()
    conn = psycopg2.connect(
        host=os.environ.get("HOST"),
        database=os.environ.get("DATABASE"),
        user=os.environ.get("USER"),
        password=os.environ.get("PASSWORD")
    )

    cursor = conn.cursor()

    query = "SELECT * FROM airflow.anime_rank;"

    cursor.execute(query)

    result = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
    json_result = [dict(zip(columns, row)) for row in result]

    cursor.close()
    conn.close()

    return json_result

def pesquisa(query: str) -> list[dict]:
    load_dotenv()
    conn = psycopg2.connect(
        host=os.environ.get("HOST"),
        database=os.environ.get("DATABASE"),
        user=os.environ.get("USER"),
        password=os.environ.get("PASSWORD")
    )

    cursor = conn.cursor()

    query = 'SELECT * FROM airflow.anime_rank WHERE "titulo_anime" ' + f"ILIKE '%{query}%';"

    cursor.execute(query)

    result = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
    json_result = [dict(zip(columns, row)) for row in result]

    cursor.close()
    conn.close()

    return json_result





