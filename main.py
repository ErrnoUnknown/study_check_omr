# 라이브러리 불러오기
import csv
import qrcode

# 사용자 지정 모듈 불러오기
import module.sql as mdl_sql
import module.image as mdl_image

# DB가 없다면 생성
mdl_sql.create_db()

# 학생 데이터 추가 함수 정의
def add_students():
    # CSV 파일 읽기
    with open('student.csv', 'r', encoding='utf-8') as file:
        # 데이터 불러오기
        reader = csv.reader(file)

        # 데이터 인덱스 없애기
        data = [row for row in reader][1:]

        for row in data:
            # 학생 데이터가 이미 존재하는지 확인
            student_exists = None != mdl_sql.get_student(name=row[0], grade=row[1], class_number=row[2], number=row[3])

            # 학생 데이터가 존재하지 않는다면 추가
            if not student_exists:
                mdl_sql.insert_student(name=row[0], grade=row[1], class_number=row[2], number=row[3])

# 출석 체크 문서 생성 함수 정의
def generate_study_check_doc():
    # 학생 데이터 가져오기
    students = mdl_sql.get_all_students()

    # 학생 정보 추가
    for index, student in enumerate(students):
        img = qrcode.make(str(student['id']), box_size=10, border=0)

        # 학생 ID QR코드 생성 및 저장
        img.save('temp/qr.png')
        mdl_image.resize_img('temp/qr.png', 'temp/qr.png', (150, 150))

generate_study_check_doc()