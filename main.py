# 라이브러리 불러오기
import csv
import qrcode

# 사용자 지정 모듈 불러오기
import module.sql as mdl_sql
import module.image as mdl_image

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
def generate_study_check_doc(study_name, year, month, date):
    # 학생 데이터 가져오기
    students = mdl_sql.get_all_students()

    # 베이스 이미지 편집
        # 결과 이미지 틀 생성
    mdl_image.create_white_image('temp/base.png', (1320, 1850))

        # 좌상단 인디케이터 추가
    mdl_image.put_image_over('temp/base.png', 'template/top_left_indicator.png', 'temp/base.png', (0, 0))

        # 우하단 인디케이터 추가
    mdl_image.put_image_over('temp/base.png', 'template/bottom_right_indicator.png', 'temp/base.png', (1270, 1800))

    # 자습 정보 QR 코드 생성 및 저장
    img = qrcode.make(f'{study_name}-{year}-{month}-{date}', box_size=10, border=0)

    img.save('temp/qr.png')
    mdl_image.resize_img('temp/qr.png', 'temp/qr.png', (100, 100))

    mdl_image.put_image_over('temp/base.png', 'temp/qr.png', 'temp/base.png', (50, 50))

    # 자습 이름 추가
    mdl_image.put_text_over(input_path='temp/base.png',
                                output_path='temp/base.png',
                                position=(175, 50),
                                text=study_name,
                                text_color=(0, 0, 0, 0),
                                size=65,
                                text_ttf_path='font/pretendard_extra_bold.ttf')
    
    # 자습 날짜 추가
    mdl_image.put_text_over(input_path='temp/base.png',
                                output_path='temp/base.png',
                                position=(175, 120),
                                text=f'{year}년 {month}월 {date}일',
                                text_color=(0, 0, 0, 0),
                                size=30,
                                text_ttf_path='font/pretendard_medium.ttf')

    # 페이지 생성
    for index, student in enumerate(students):
        # 학생 ID QR 코드 생성 및 저장
        img = qrcode.make(str(student['id']), box_size=10, border=0)

        img.save('temp/qr.png')
        mdl_image.resize_img('temp/qr.png', 'temp/qr.png', (100, 100))

        mdl_image.put_image_over('temp/base.png', 'temp/qr.png', 'temp/result.png', (50, (index * 150) + 300))

        # 이름 추가
        mdl_image.put_text_over(input_path='temp/result.png',
                                output_path='temp/result.png',
                                position=(170, (index * 150) + 300),
                                text=student['name'],
                                text_color=(0, 0, 0, 0),
                                size=30,
                                text_ttf_path='font/pretendard_extra_bold.ttf')

        # 학적 추가
        mdl_image.put_text_over(input_path='temp/result.png',
                                output_path='temp/result.png',
                                position=(170, (index * 150) + 340),
                                text=f'{student["grade"]}학년 {student["class_number"]}반 {student["number"]}번',
                                text_color=(0, 0, 0, 0),
                                size=30,
                                text_ttf_path='font/pretendard_medium.ttf')

# DB가 없다면 생성
mdl_sql.create_db()

add_students()
generate_study_check_doc('심야 자율학습', 2008, 2, 25)