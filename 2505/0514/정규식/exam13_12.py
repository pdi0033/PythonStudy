import re

contents = """
    우리커피숍 100-90-12345
    영풍문고 101-91-12121
    영미청과 102-92-23451
    황금코인 103-89-13579
    우리문구 104-91-24689
    옆집회사 105-82-12345
"""

pattern = r"\b(\d{3})-(\d{2})-(\d{5})\b"
matchObj = re.finditer(pattern, contents)

for item in matchObj:
    print(item.group(), end='\t')
    if item.group(2) >= "90" and item.group(2) <= "99":
        print("이 번호는 개인 면세 사업자 번호입니다.")
    else:
        print()
