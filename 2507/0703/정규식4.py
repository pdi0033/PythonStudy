import re

text1 = "I like star, red star, yellow star"
text2 = "starship is beautiful"

pattern = "star"
print(re.search(pattern, text1))     # 첫번째 star만 찾는다.
print(re.search(pattern, text2))     

matchObject = re.search(pattern, text2)
print(matchObject.group())
print(matchObject.start())
print(matchObject.end())
print(matchObject.span())

print(text2[:4])



