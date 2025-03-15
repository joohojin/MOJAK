import re

def main():
    with open("data/p5_rect_code.js", "r", encoding="utf-8") as f:
        code = f.read()

    # rect 코드 정리
    code = re.sub(r"rect\((\d+), (\d+), (\d+), (\d+)\);", r"rect(\1*s, \2*s, s, s);", code)

    # 파일로 저장
    with open("data/p5_rect_code_s.js", "w", encoding="utf-8") as out:
        out.write(code)

if __name__ == "__main__":
    main()
    