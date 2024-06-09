# 라이브러리 불러오기
import cv2

def resize_img(input_path, output_path, size):
    img = cv2.imread(input_path)
    img = cv2.resize(img, size)
    cv2.imwrite(output_path, img)