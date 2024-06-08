# Import
import sqlite3

# Define SQL decorator
def sql_decorator(func):
    def decorated(*args, **kwargs):
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()

        func(cursor=cursor, *args, **kwargs)

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
        grade INTEGER NOT NULL,
        class_number INTEGER NOT NULL,
        number INTEGER NOT NULL,
        check_date TEXT
    );
    '''

    cursor.execute(query)

@sql_decorator
def insert_student(cursor, name, grade, class_number, number):
    query = '''
    INSERT INTO student(name, grade, class_number, number, check_date)
    VALUES (?, ?, ?, ?, ?)
    '''

    cursor.execute(query, (name, grade, class_number, number, ''))