import os
import psycopg2
from dotenv import load_dotenv

def get_user(id: int) -> dict:
    load_dotenv()
    query = f"""
        select 
            login.username,
            login.email,
            users.*
        from airflow.login as login
        join airflow.usuarios as users
            on users.user_id = login.user_id
        where login.user_id = {id}
        """
    try:
        conn = psycopg2.connect(
            host=os.environ.get("HOST"),
            database=os.environ.get("DATABASE"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD")
        )

        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        column_names = [desc[0] for desc in cursor.description]
        result_dict = dict(zip(column_names, result))

        return result_dict
    except Exception as e:
        print(f"Erro durante a inserção: {e}")
        return 0
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def create_user(username, email, password) -> int:
    import random
    load_dotenv()
    numero_aleatorio = random.randint(1, 100000)

    insert_query = """
        INSERT INTO airflow.login (user_id, username, password, email)
        VALUES (%s, %s, %s, %s);
    """
    insert_user = F"""
        INSERT INTO airflow.usuarios
        VALUES ({numero_aleatorio}, '', '', '');
    """
    try:
        conn = psycopg2.connect(
            host=os.environ.get("HOST"),
            database=os.environ.get("DATABASE"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD")
        )

        cursor = conn.cursor()
        cursor.execute(insert_query, (numero_aleatorio, username, password, email))
        cursor.execute(insert_user)
        conn.commit()

        print("Inserção realizada com sucesso!")
        return numero_aleatorio
    except Exception as e:
        print(f"Erro durante a inserção: {e}")
        return 0
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def logar(email, password) -> dict:

    load_dotenv()

    insert_query = """
        select log.user_id
        from airflow.login as log
        where log.email = %s and log.password = %s;
    """
    try:
        conn = psycopg2.connect(
            host=os.environ.get("HOST"),
            database=os.environ.get("DATABASE"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD")
        )

        cursor = conn.cursor()
        cursor.execute(insert_query, (email, password))
        result = cursor.fetchone()
        column_names = [desc[0] for desc in cursor.description]
        result_dict = dict(zip(column_names, result))

        return result_dict
    except Exception as e:
        print(f"Erro durante a inserção: {e}")
        return 0
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
