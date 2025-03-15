from PIL import Image

def main():
    # 1. data 폴더에 있는 skull.png 이미지 열기
    img = Image.open("data/skull.png").convert("RGBA")
    
    # 2. 이미지 크기(너비, 높이) 가져오기
    width, height = img.size
    
    # 3. 픽셀 데이터 읽어오기 (r, g, b, a) 형태로 너비*높이 만큼 생김
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
    
    # 5. data/source.txt 파일에 저장
    with open("data/source.txt", "w", encoding="utf-8") as out:
        out.write(str(pixel_array))

if __name__ == "__main__":
    main()
