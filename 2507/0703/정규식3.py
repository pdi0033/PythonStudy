import re

text1 = "I like star"
text2 = "starship is beautiful"

pattern = "star"
print(re.match(pattern, text1))     # none
print(re.match(pattern, text2))     

matchObject = re.match(pattern, text2)
print(matchObject.group())
print(matchObject.start())
print(matchObject.end())
print(matchObject.span())

print(text2[:4])



