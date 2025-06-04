# list 타입 => 배열
# 인덱싱과 슬라이싱을 지원한다.
words = ["red", "green", "blue"]
print(words)    # 한 번에 출력 가능
print(words[0])
print(words[:2])

# 새로운 단어 추가
# .append()
words.append("black")
words.append("cyan")
print(words)
print("단어 개수: ", len(words))
print("red 개수: ", words.count("red"))
print("red 위치: ", words.index("red")) # list에는 find가 안 된다. index로 위치를 찾아야 한다.

if words.count("yellow") :
    print("yellow 위치: ", words.index("yellow"))
else:
    print("yellow는 없다.")

# in 연산자
# "내용" in list 타입 있으면 True 없으면 False를 반환하다.
if "yellow" in words :
    print("yellow 위치: ", words.index("yellow"))
else:
    print("yellow는 없다.")

print(words[::-1])

# 인덱싱 - list 타입의 경우에는 인덱싱을 통해 값 변경 가능.
# 하지만 문자열은 indexing을 통해 값 변경 불가.
words[0] = "white"
print(words)

s = "white"
#s[0] = "W"     # 문자열의 경우는 인덱싱을 통한 값 변경은 불가능하다.
s = s.replace("w", "W")
print(s)
s2 = "W" + s[1:]
print(s2)

# extend 함수 - 리스트와 리스트를 합친다.
# words.extend("brown")     # 'b','r','o','w','n'로 들어간다.
words.extend(["brown", "violet", "puple", "magenta"])
print(words)

# list 타입을 str 타입으로. 
# .join()을 사용한다.
s = ", ".join(words)
print(s)

# str 타입을 list로
# .split()
words2 = s.split(", ")
print(words2)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0])
print(numbers[:2])
print(numbers[::-1])
print(numbers[1::2])

# 리스트 만들기
names = []      # names = list()    동일한 문법이다.
names.append("홍길동")
names.append("임꺽정")
names.append("장길산")
names.append("홍경래")
print(names)

names = list()
names.append("모란")
names.append("작약")
names.append("불두화")
names.append("목련")
print(names)


