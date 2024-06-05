# Import
import sqlite3

# Define SQL decorator
def sql_decorator(func):
    def decorated():
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()

        func(cursor)

        conn.commit()
        conn.close()

    return decorated

# Create DB
@sql_decorator
def create_db(cursor):
    query = '''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        class INTEGER NOT NULL,
        number INTEGER NOT NULL,
        check_date TEXT
    );
    '''

    cursor.execute(query)