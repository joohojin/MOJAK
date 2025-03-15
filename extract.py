from PIL import Image

def main():
    # 1. 동일 폴더 내의 이미지 파일 열기
    img = Image.open("skull.png").convert("RGBA")
    
    # 2. 이미지 크기(너비, 높이) 가져오기
    width, height = img.size
    
    # 3. 픽셀 데이터 읽어오기 (getdata() 사용)
    #    -> (r, g, b, a) 형태로 너비*높이 만큼 생김
    pixels = list(img.getdata())
    
    # 4. 2차원 배열로 변환
    pixel_array = []
    for y in range(height):
        row = []
        for x in range(width):
            idx = y * width + x
            r, g, b, a = pixels[idx]
            row.append([r, g, b, a])  # RGBA
        pixel_array.append(row)
    
    # 5. source.txt 파일에 저장
    with open("source.txt", "w", encoding="utf-8") as f:
        for row in pixel_array:
            for pixel in row:
                f.write(f"{pixel[0]} {pixel[1]} {pixel[2]} {pixel[3]}\n")

