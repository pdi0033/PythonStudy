import re

contents = "문의사항이 있으면 010-1234-6789 으로 연락주시기 바랍니다."
pattern = r"\b(\d{2,3})-(\d{3,4})-(\d{4})\b"
regex = re.compile(pattern)
result = regex.search(contents)
print()

if result != None:
    phone1 = result.group(1)
    phone2 = result.group(2)
    phone3 = result.group(3)
    print(phone1)
    print(phone2)
    print(phone3)
else:
    print("전화번호가 없습니다.")

result = re.finditer(pattern, contents)
for item in result:
    print(item.group(1))
    print(item.group(2))
    print(item.group(3))