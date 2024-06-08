# Import libs
import csv

# Import modules
from module.sql import *

# Init DB if not exists
create_db()

# CSV 파일 읽기
with open('student.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    data = [row for row in reader][1:]

    for row in data:
        print(f'이름: {row[0]}')
        print(f'학년: {row[1]}')
        print(f'반: {row[2]}')
        print(f'번호: {row[3]}')
        print('=' * 10)
        print()

        insert_student(name=row[0],
                       grade=row[1],
                       class_number=row[2],
                       number=row[3])