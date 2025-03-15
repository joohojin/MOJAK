import json

def main():
    with open("source.txt", "r", encoding="utf-8") as f:
        pixel_array = json.load(f)
    
    pixel_size = 1

    # 파일로 저장
    with open("p5_rect_code.js", "w", encoding="utf-8") as out:
        for y in range(len(pixel_array)):
            for x in range(len(pixel_array[y])):
                r, g, b, a = pixel_array[y][x]
                out.write(f"fill({r}, {g}, {b}, {a});\n")
                out.write(f"rect({x * pixel_size}, {y * pixel_size}, {pixel_size}, {pixel_size});\n")