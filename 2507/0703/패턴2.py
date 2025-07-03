import re

pattern = r"\b(\d{3})-(\d{2})-(\d{5})\b"

contents = """
    우리커피숍 100-90-12345
    영풍문고 101-91-12121
    영미청과 102-92-23451
    황금코인 103-89-13579
    우리문구 104-91-24689
    옆집회사 105-82-12345
"""

regex = re.compile(pattern)
result = regex.finditer(contents)

for it in result:
    if it.group(2) >= "90" and it.group(2) <= "99":
        print(it.group())

