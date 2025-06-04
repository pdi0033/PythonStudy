# 튜플
a = (1,2,3,4,5)
print(a, type(a))

a = 5
b = 7
c = 9

a,b,c = 5,7,9   # tuple 활용. (a,b,c) = (5,7,9)와 동일하다.
print(a,b,c)

# 함수
# 값을 여러 개를 반환할 때 자동으로 튜플로 만들어 튜플 하나로 반환한다.
def myFunc1():
    return 3,4
a = myFunc1()
print(a, type(a))

b, c = a
print(b, c, type(b), type(c))

# 두 개의 변수 값을 서로 exchange, swap
# 튜플을 사용해서 쉽게 swap할 수 있다.
a = 5
b = 7
a, b = b, a
print(a, b)

# 튜플은 요소의 수정/추가/삭제 불가.
a = (1,2,3,4,5,6,7,8,9,10)
print(a[0])
print(a[1])
print(a[2])
# del a[2]        # TypeError: 'tuple' object doesn't support item deletion
# a[0] = 11       # TypeError: 'tuple' object does not support item assignment

print(a[:5])
print(a[2:5])
print(a[::-1])

b = a + a
print(b, type(b))

b = a * 3
print(b)