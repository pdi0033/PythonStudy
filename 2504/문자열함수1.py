# .count("")
# 문자열 안에 찾는 문자열이 몇 개 있는지 세는 함수
s = "hobby"
print(s.count("b")) 
print(s.count("t"))

# .find("")
# 문자의 위치 값을 찾는 함수
print(s.find("b"))  # 첫번쨰 문자 위치 값을 반환
print(s.find("K"))  # 없으면 -1을 반환

s = "I like star. red star. blue star. I like star."
print(s.count("star"))
print(s.find("star"))

pos1 = s.find("star")
print(pos1)

pos2 = s.find("star", pos1+1)   # 1번째 star 찾은 그 다음부터 찾아라
print(pos2)

# .index("")
# 위치를 찾아준다.
pos1 = s.index("like")
print(pos1)
# pos2 = s.index("love")  # 단어가 없으면 예외(오류)가 발생한다.
# print(pos2)

# .join("") 문자열 결합
# []에 전달된 단어들을 처음 ","이 안에 있는 기호로 묶어서 문장으로 만들어주는 역할을 한다.
s = ",".join("abcd")
print(s)
s = ",".join(["cherry", "banana", "pear", "grape"])
print(s)

# .split("")
# 하나의 문장을 쪼갠다. > list 타입으로 반환한다.
words = s.split(",")
print(words)

# .upper() >> 소문자를 대문자로
# .lower() >> 대문자를 소문자로
print("hi".upper())
print("HI".lower())

# 공백 지우기
# .lstrip() >> 왼쪽 공백 지우기
# .rstrip() >> 오른쪽 공백 지우기
# .strip() >> 양 옆쪽 공백 지우기
print("*" + "     Hello World!!!      ".lstrip() + "*")
print("*" + "     Hello World!!!      ".rstrip() + "*")
print("*" + "     Hello World!!!      ".strip() + "*")

# .replace("바꿔지는 문자", "대체되는 문자")
str1 = "My life is good"
str2 = str1.replace("good", "bad")
print(str1)
print(str2)

# .isalpha() >> 알파벳으로만 이루어져 있나
print("Python".isalpha())
print("Python3".isalpha())
print("Python".isdigit())
print("123".isdigit())

# 자기 자신은 바뀌지 않는다.
# 바뀐 값을 반환할 뿐이다.
s = "hello"
print(s.upper(), s)
s = s.upper()
print(s)


