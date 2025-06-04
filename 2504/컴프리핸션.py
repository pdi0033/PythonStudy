# 컴프리핸션
# 소프트 카피
a = [1,2,3,4,5,6,7,8,9,10]
b = a
a[2] = -3

print(a)
print(b)

# 사용자가 구현한 하드 카피 상황
b = []  # 새로 기억 공간을 만든다.
for item in a:      # a로부터 데이터를 하나씩 가져와서 item이라는 변수에 저장한다.
    b.append(item)
b[3] = 99 
print(a)
print(b)

# 하드 카피
# 컴프리핸션 => 리스트 복사에 자주 사용한다.   [변수명 for 변수명 in 리스트형_변수]
c = [item for item in a]
c[5] = 55
print(a)
print(c)

d = [item * 2 for item in a]
print("d=", d)

# 조건을 부여할 수도 있다.
# [변수명 for 변수명 in 리스트형_변수   if 변수명 > 0]
# a의 숫자를 짝수와 홀수로 나눠보자
oddList = [ x for x in a if x%2 == 1]
print(oddList)

# 문자열도 가능하다.
wordList = ["rain", "desk", "hospital", "building", "java", "python", "cloud", "rainbow", "assembly",
            "javascript", "html", "css"]
# 1. 하드 카피
wordList2 = [ w for w in wordList ]
print(wordList2)

# 2. 복사하면서 대문자로 바꾸고 싶다.
wordList3 = [ w.upper() for w in wordList ]
print(wordList3)

# 3. 단어와 단어 길이를 짝으로
wordList3 = [ (w, len(w), w.upper()) for w in wordList ]
print(wordList3)

# 4. 단어 길이가 5 글자 이상인 것만
wordList3 = [ w for w in wordList if len(w) >= 5]
print(wordList3)


# 문제1. 단어 중에 java라는 단어가 있는 것만 추출하기
# wordList3 = [ w for w in wordList if w.find("java") >= 0]
wordList3 = [ w for w in wordList if "java" in w]
print(wordList3)

# 문제2. 단어 중에 길이가 5개보다 짧은 단어만 추출하기
wordList3 = [ w for w in wordList if len(w) < 5]
print(wordList3)