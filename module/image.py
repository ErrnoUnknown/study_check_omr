# 라이브러리 불러오기
import cv2
import numpy as np

# 이미지 크기 재조정 함수 정의
def resize_img(input_path, output_path, size):
    img = cv2.imread(input_path)
    img = cv2.resize(img, size)
    cv2.imwrite(output_path, img)

# 이미지 생성 함수 정의
def create_white_image(output_path, size):
    img = np.ones((size[1], size[0], 3), dtype=np.uint8) * 255
    cv2.imwrite(output_path, img)

# 이미지 오버레이 함수 정의
def put_image_over(bg_input_path, overlay_input_path, output_path, position):
    bg_img = cv2.imread(bg_input_path)
    overlay_img = cv2.imread(overlay_input_path)

    overlay_height, overlay_width = overlay_img.shape[:2]

    x, y = position

    bg_img[y:y+overlay_height, x:x+overlay_width] = overlay_img

    cv2.imwrite(output_path, bg_img)