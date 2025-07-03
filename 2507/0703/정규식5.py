import re

text = """
    홍길동 phone : 010-0000-0000 email:test1@nate.com
    임꺽정 phone : 010-1111-1111 email:         test2@naver.com
    장길산 phone : 010-2222-2222 email: test3@gmail.com
"""

# ^ 시작하는    $ 끝나는     \b 경계가 있는
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b'
matchObject = re.findall(pattern, text)
print(matchObject)

phonePattern = r'\b\d{2,3}-\d{3,4}-\d{4}\b'
matchObject = re.findall(phonePattern, text)
print(matchObject)

matchObject = re.finditer(pattern, text)
for ob in matchObject:
    print(ob)
