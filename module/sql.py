# 라이브러리 불러오기
import sqlite3

# SQL 데코레이터 정의
def sql_decorator(func):
    def decorated(*args, **kwargs):
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()

        result = func(cursor=cursor, *args, **kwargs)

        conn.commit()
        conn.close()

        return result

    return decorated

# DB가 존재하지 않을 경우 생성하는 함수
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

# 학생 추가 함수 정의
@sql_decorator
def insert_student(cursor, name, grade, class_number, number):
    query = '''
    INSERT INTO student(name, grade, class_number, number, check_date)
    VALUES (?, ?, ?, ?, ?)
    '''

    cursor.execute(query, (name, grade, class_number, number, ''))

# 학생 데이터를 불러오는 함수 정의
@sql_decorator
def get_student(cursor, name, grade, class_number, number):
    query = '''
    SELECT * FROM student
    WHERE name = ? AND grade = ? AND class_number = ? AND number = ?
    '''

    cursor.execute(query, (name, grade, class_number, number))

    result = cursor.fetchone()

    if result == None:
        return None

    return {'id': result[0],
            'name': result[1],
            'grade': result[2],
            'class_number': result[3],
            'number': result[4],
            'check_date': result[5]}