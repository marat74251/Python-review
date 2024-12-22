import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


def get_connection():
    return psycopg2.connect(
        dbname = DB_NAME,
        user = DB_USER,
        password = DB_PASSWORD,
        host = DB_HOST,
        port = DB_PORT
    )

def create_table():
    conn = get_connection()
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS my_table (name TEXT NOT NULL, data TEXT NOT NULL);")
        conn.commit()
    conn.close()

def get_data():
    conn = get_connection()
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM my_table;")
        result = cursor.fetchall()
    conn.close()
    return result

def val_get():
    conn = get_connection()
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT data FROM my_table;")
        result = cursor.fetchone()
    conn.close()
    return result

def save_data_for_head(data):
    conn = get_connection()
    flattened_data = [(item[0], item[1]) for item in data]
    with conn.cursor() as cursor:
        insert_query = "INSERT INTO my_table (name, data) VALUES (%s, %s);"
        cursor.executemany(insert_query, flattened_data)
        conn.commit()
    conn.close()

def delete_data():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM my_table;")
        conn.commit()
    conn.close
