data = """
park 800905-1049118  park@hanmail.com
kim  700905-1059119  kim@naver.com
Life is egg
kim  700906-1059118  kim9999@naver.com
"""

result = []
for line in data.split("\n"):
    print(line)
    word_result = []
    for word in line.split(" "):
        print(word)
        # len(word) - 문자열의 길이가 14자
        # - 앞의 6자리가 숫자여야 한다. word[:6] 0~5번방까지 전체 숫자로만 구성되어 있느냐
        # - 뒤의 6자리가 숫자여야 한다. word[7:] 7번부터 마지막까지 전체 숫자로만 구성되어 있느냐
        # word[6] == '-' 조건을 추가할 수도 있다.
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():   # 주민번호 패턴이 맞다고 한다면
            word = word[:6] + "-" + "*******"
            # 앞자리 6자리 + - + *******
        word_result.append(word)
    result.append(" ".join(word_result))    # 같은 라인 주민번호를 공백으로 연결시켜 리스트에 더함

print("\n".join(result))


import re

pat = re.compile("(\d{6})[-]\d{7}")     #\d숫자 {6} 여섯자리 [-] \d{7}
print(pat.sub("\g<1>-*******", data))