import re

zipcode = input("우편번호를 입력하세요. >>")
#pattern = r"\d{5}$"             # $가 끝내는 기호. 정수 다섯자리로 끝나는.
pattern = r"colou?r"
regex = re.compile(pattern)     # match 시작 단어에 매칭하는 값이 있어야 한다.
result = regex.match(zipcode)   # 일치 안 하면 None 반환. 일치하면 match객체 반환.
if result != None:
    print("형식이 일치합니다.")
    print(result)
else:
    print("잘못된 형식입니다.")