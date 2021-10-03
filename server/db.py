import os
import sqlite3
import psycopg2


_connection = None
_db_initialized = None


def get_connection():
    global _connection
    if _connection:
        return _connection
    if os.getenv('USE_POSTGRES'):

        _connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME", 'blog'),
            user=os.getenv("DB_USER", 'postgres'),
            password=os.getenv("DB_PASSWORD", 'root'),
            host=os.getenv("DB_HOST", 'postgres'),
            port=os.getenv("DB_PORT", 5432),
        )
    else:
        _connection = sqlite3.connect('blog.db')
    _initialize_db(_connection)
    return _connection


def _initialize_db(connection):
    global _db_initialized
    if _db_initialized:
        return
    cursor = connection.cursor()
    if os.getenv('USE_POSTGRES'):
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                   (id_ SERIAL PRIMARY KEY , title TEXT, text TEXT, published BOOLEAN)''')
    else:
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                   (id_ INTEGER PRIMARY KEY AUTOINCREMENT , title TEXT, text TEXT, published BOOLEAN)''')
    connection.commit()
