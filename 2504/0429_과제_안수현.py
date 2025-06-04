# 오늘의 과제
words = ["assembly", "java", "rain", "notebook", "north",
        "south", "hospital", "programming", "house", "hour" ]

# 문제1. filter를 사용해서 글자수가 6글자 이상인 단어만 출력하기 (컴프리핸션 X)
print("문제1")
for i in filter(lambda x: len(x) >= 6, words):
    print(i)

# x에 전달되는 건 string 타입이다. len(x) 문자열 길이
resultList = list( filter(lambda x : len(x)>= 6, words) )
print(resultList)
print()

# 문제2. map 함수를 사용해서 글자를 대문자로 바꾸어서 출력하기  (컴프리핸션 X)
print("문제2")
def map_upper(w):
    s = ""
    for i in map(lambda x: x.upper(), w):
        s += i
    return s

for i in words:
    pass
    #print(map_upper(i))

resultList = list( map(lambda x : x.upper(), words) )
print(resultList)
print()

# 문제3. sorted 함수를 사용하여 단어들의 길이순으로 오름차순 정렬하여 출력하기
print("문제3")
sortedWords = sorted(words, key= lambda x: len(x))
for i in sortedWords:
    print(i)
print()

# 문제4. sorted 함수를 사용하여 알파벳 수능로 내림차순으로 정렬하여 출력하기
print("문제4")
sortedWords = sorted(words, reverse=True)
for i in sortedWords:
    print(i)
print()

# 문제5. 단어중에 o가 포함되는 단어가 모두 몇 개인지 카운트하기 (힌트, filter를 사용)
print("문제5")
def has_o(w):
    for i in filter(lambda x: x == "o", w):
        return True
    return False

cnt = 0
for i in words:
    if has_o(i):
        cnt += 1

resultList = list(filter(lambda w: "o" in w, words))
print(len(resultList))
print(f"o가 포함된 문자는 {cnt}개 입니다.")