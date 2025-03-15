#다음은 p5_rect_code.js를 불러와서 정리하는 코드입니다

# fill(19, 15, 11, 255);
# rect(0, 0, 1, 1);

#위와같은 형식이 있으면, rect의 안에 들어있는 숫자를 정리합니다.

# rect에 들어있는 숫자는 x, y, width, height 순서로 들어있으며, 이를 픽셀 사이즈를 원하는 값으로 바꿀 수 있도록 하는 알고리즘을 추가합니다.

# 예시로 s라는 변수를 추가하여 s를 pixel_size로 바꾸어서 rect의 width와 height를 s를 곱해줍니다.

# 즉 코드는 다음과 같이 바뀝니다.

# rect(0, 0, 1, 1); -> rect(0*s, 0*s, s, s);

#이렇게 된다면 s를 10으로 설정하면 rect(0, 0, 1, 1); -> rect(0*10, 0*10, 10, 10); 이 되어 10*10의 크기로 출력됩니다.

#이렇게 p5_rect_code.js를 불러와서 rect에 s를 추가해주는 코드를 작성해보겠습니다. 또한 완성된 코드는 p5_rect_code_s.js로 저장합니다.

import re

def main():
    with open("p5_rect_code.js", "r", encoding="utf-8") as f:
        code = f.read()

    # rect 코드 정리
    code = re.sub(r"rect\((\d+), (\d+), (\d+), (\d+)\);", r"rect(\1*s, \2*s, s, s);", code)

    # 파일로 저장
    with open("p5_rect_code_s.js", "w", encoding="utf-8") as out:
        out.write(code)

if __name__ == "__main__":
    main()

#이렇게 작성하면 p5_rect_code.js를 불러와서 rect에 s를 추가해주는 코드를 작성할 수 있습니다. 또한 완성된 코드는 p5_rect_code_s.js로 저장됩니다.
