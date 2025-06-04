a = [1,2,3,4]
b = [5,6,7,8]

# 리스트를 결합하는 방법 
# 원본을 안 바꾸고 더해진 새로운 list를 반환
c = a + b   # 연산자 중복 기능 => 우리가 연산자를 새로 만들 수 있다.
print(c)

a.extend(b) # 원본에 추가
print(a)

s = "hello"
if s == "hello":    # if s.equals("hello") -- java
    print("같다")
else:
    print("다르다")

# 요소 삭제
# del 삭제할 요소
del c[0]
print(c)

del c[4:]   # 4번째 요소 이후로 모두 삭제를 하라
print(c)

# .sort()   정렬
# 기본적으로 오름차순으로 정렬한다.
a = [4,3,5,7,9,1,11,17,12,15,8]
a.sort()    # 정렬: 순서대로 데이터를 늘어놓는 것을 말한다.
print(a)
a.reverse() # 순서 뒤집기. 여기서 정렬한 것을 뒤집었기 때문에 내림차순이 되었다.
print(a)

# .insert(넣을 위치, 넣을 요소) - 특정 위치에 데이터 끼워 넣기
a.insert(0, 100)    # 0번째 위치에 값 100 넣기
print(a)
a.insert(5, 77)     # 5번째 위치에 값 77 넣기
print(a)
a.insert(len(a), 88)    # 마지막 위치에 값 88 넣기. append() 함수와 동일한 역할을 한다.
print(a)

# .remove(삭제할 값)    - 값을 찾아서 첫 번째로 나오는 값을 찾아서 삭제.
a.remove(77)
print(a)

# .pop()    - 마지막 요소를 반환하고 그 요소를 삭제한다.
a = []
a.append("A")    # 스택 구조의 push 동작
a.append("B")
a.append("C")
a.append("D")
a.append("E")
print(a)

print(a.pop())  # 마지막 것을 끄집어 낸다.
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)

