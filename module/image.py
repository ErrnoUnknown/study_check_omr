# 라이브러리 불러오기
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 이미지 크기 재조정 함수 정의
def resize_img(input_path, output_path, size):
    # 이미지 열기
    img = cv2.imread(input_path)

    # 이미지 처리
    img = cv2.resize(img, size)

    # 이미지 저장
    cv2.imwrite(output_path, img)

# 이미지 생성 함수 정의
def create_white_image(output_path, size):
    # 이미지 생성
    img = np.ones((size[1], size[0], 3), dtype=np.uint8) * 255

    # 이미지 저장
    cv2.imwrite(output_path, img)

# 이미지 오버레이 함수 정의
def put_image_over(bg_input_path, overlay_input_path, output_path, position):
    # 이미지 열기
    bg_img = cv2.imread(bg_input_path)
    overlay_img = cv2.imread(overlay_input_path)

    # 이미지 처리
    overlay_height, overlay_width = overlay_img.shape[:2]

    x, y = position

    bg_img[y:y+overlay_height, x:x+overlay_width] = overlay_img

    # 이미지 저장
    cv2.imwrite(output_path, bg_img)

# 텍스트 오버레이 함수 정의
def put_text_over(input_path, output_path, position, text, text_color, size, text_ttf_path):
    # 이미지 열기
    img = Image.open(input_path)

    # 폰트 열기
    font = ImageFont.truetype(text_ttf_path, size)

    # 이미지 처리
    draw = ImageDraw.Draw(img)
    draw.text(position, text, font=font, fill=text_color)

    # 이미지 저장
    img.save(output_path)