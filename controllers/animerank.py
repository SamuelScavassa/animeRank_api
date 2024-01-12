import psycopg2
import json

def lista() -> list[dict]:
    conn = psycopg2.connect(
        host="192.168.1.80",
        database="postgres",
        user="postgres",
        password="samuel04"
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
    conn = psycopg2.connect(
        host="192.168.1.80",
        database="postgres",
        user="postgres",
        password="samuel04"
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

def create_user(username, email, password) -> int:
    import random

    numero_aleatorio = random.randint(1, 100000)

    insert_query = """
        INSERT INTO airflow.login (user_id, username, password, email)
        VALUES (%s, %s, %s, %s);
    """

    # Conectando ao banco de dados e executando o INSERT
    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect(
            host="192.168.1.80",
            database="postgres",
            user="postgres",
            password="samuel04"
        )
        # Criar um cursor para executar a consulta
        cursor = conn.cursor()

        # Executar o INSERT usando parâmetros
        cursor.execute(insert_query, (numero_aleatorio, username, password, email))

        # Commit para efetivar a transação
        conn.commit()

        print("Inserção realizada com sucesso!")
        return numero_aleatorio
    except Exception as e:
        print(f"Erro durante a inserção: {e}")
        return 0
    finally:
        # Fechar cursor e conexão
        if cursor:
            cursor.close()
        if conn:
            conn.close()




