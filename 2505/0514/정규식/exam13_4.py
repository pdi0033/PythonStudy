import re

#전화번호만 추출하기
text = """
    phone : 010-0000-0000 email: test1@nate.com
    phone : 010-1111-1111 email: test2@naver.com
    phone : 010-2222-2222 email: test3@gmail.com
    phone : 02-345-9090   email: asdadseisk@hanmail.netwdsweds
"""
print()
print("---- 전화번호 추출하기 ----")
phonePattern = r"\d{2,3}-\d{3,4}-\d{4}"

matchObj = re.findall(phonePattern, text)

for item in matchObj:
    print(item)
    
print("---- 이메일 추출하기 ----")
# \b를 붙이지 않으면 asdadseisk@hanmail.netwdsweds 는 찾지 않는다.
# \b는 boundary(경계)라는 뜻
# 탭, 공백, 줄바꿈 기호 등으로 경계가 구분되어야 matching여부를 판단한다.
emailPattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b"

matchObj = re.findall(emailPattern, text)
for item in matchObj:
    print(item)
print()