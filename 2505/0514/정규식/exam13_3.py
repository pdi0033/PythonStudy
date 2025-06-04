import re

text1 = "I like stars, red star, yellow star"
text2 = "star is beautiful"

pattern = "star"       #match 함수
print(re.search(pattern, text1))     #None, 뒤에 있어선 안 된다.
print(re.search(pattern, text2))

matchObj = re.search(pattern, text1)
print(matchObj.group())
print(matchObj.start())
print(matchObj.end())
print(matchObj.span())

matchObj = re.search(pattern, text2)
print(matchObj.group())
print(matchObj.start())
print(matchObj.end())
print(matchObj.span())