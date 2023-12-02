# 함수 저장을 위한 파일
from PIL import Image

def make_color_transparent(obj, file_, target_color):
    # 이미지의 너비와 높이
    width = obj.image.w
    height = obj.image.h

    # 이미지 객체로 생성
    im = Image.open(file_)

    # RGB 모드로 변경
    rgb_im = im.convert('RGB')

    # 대상 색상을 투명하게 만들기
    for y in range(height):
        for x in range(width):
            r, g, b, a = rgb_im.getpixel(x, y)
            if (r, g, b) == target_color:
                obj.image.set_pixel(x, y, (0, 0, 0, 0))  # 투명한 픽셀


