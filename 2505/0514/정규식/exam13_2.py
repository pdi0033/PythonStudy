import re

text1 = "I like star"
text2 = "starship is beautiful"

pattern = "star"       #match 함수
print(re.match(pattern, text1))     #None, 뒤에 있어선 안 된다.
print(re.match(pattern, text2))

matchObj = re.match(pattern, text2)
print(matchObj.group())
print(matchObj.start())
print(matchObj.end())
print(matchObj.span())