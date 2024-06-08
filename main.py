# 라이브러리 불러오기
import csv

# 사용자 지정 모듈 불러오기
from module.sql import *

# DB가 없다면 생성
create_db()

# CSV 파일 읽기
with open('student.csv', 'r', encoding='utf-8') as file:
    # 데이터 불러오기
    reader = csv.reader(file)

    # 데이터 인덱스 없애기
    data = [row for row in reader][1:]

    for row in data:
        # 학생 데이터가 이미 존재하는지 확인
        student_exists = None != get_student(name=row[0], grade=row[1], class_number=row[2], number=row[3])

        # 학생 데이터가 존재하지 않는다면 추가
        if not student_exists:
            insert_student(name=row[0], grade=row[1], class_number=row[2], number=row[3])