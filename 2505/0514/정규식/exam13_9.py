import re

pattern = r"[p|P]ython"     #문장 중에 python 또는 Python

text = ["python", "Python", "PYTHON", "12python", "Python3"]
repattern = re.compile(pattern)

for item in text:
    result = repattern.search(item)
    if result:
        print(item, "-- O")
    else:
        print(item, "-- X")

print("-"*8)

pattern = r"[A-Z]"      # 문장 중 대문자가 하나라도 포함되면

text = ["python", "Python", "PYTHON", "12python", "Python3", "korea", "KOREA", "koR3A"]
repattern = re.compile(pattern)

for item in text:
    result = repattern.search(item)
    #match 함수는 첫 시작만을 보기 때문에 적용 안됨
    if result:
        print(item, "-- O")
    else:
        print(item, "-- X")