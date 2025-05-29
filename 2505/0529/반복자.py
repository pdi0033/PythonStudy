a = [10,20,30,40]
print(a[0])
it = iter(a)        # 반복자 객체를 반환한다.
print(next(it))
print(next(it))
# 위의 iter와 같다.
for i in a:
    print(i)

b = {"red": "빨간색", "green": "초록색", "blue": "파란색"}
it2 = iter(b)
print(next(it2))
print(next(it2))
print(next(it2))

# 반복자 가져오는 또다른 방법
# __시작하는 함수들은 내장함수
it = a.__iter__()
print(next(it))     # 반복자의 현재 위치값을 반환하고 반복자가 다음번 요소로 이동
# 더이상 읽을 데이터가 없으면 파이썬의 경우에는 StopIteration이라는 예외를 발생시킨다.
# 보통은 이렇게 쓰지 말고, for문을 쓰는 게 좋다.
for i in a:
    print(i)

it = a.__iter__()
while True:
    try:
        item = next(it)     # 현재 가리키는 데이터를 반환하고 다음 요소로 이동
        print(item)
    except StopIteration:
        print("이터레이터 종료")
        break

# 이런 거 가능하게 하기 위해서 반복자라는 개념을 사용했다.
for i in a:
    print(i)

print("-" * 15)
class MyInterface:
    def __init__(self, add=None, sub=None):
        self.add = add     # 함수
        self.sub = sub

class MyCalculator(MyInterface):
    def __init__(self):
        self.add = self.add2
        self.sub = self.sub2

    def add2(self, x,y):
        return x+y
    
    def sub2(self, x,y):
        return x-y

def add(x, y):
    return x+y
def sub(x, y):
    return x-y

m1 = MyInterface(add, sub)
print(m1.add(10, 5))
print(m1.sub(10, 5))

m1 = MyCalculator()
print(m1.add(10, 5))
print(m1.sub(10, 5))


"""
MyIterface iis = new Mycalculator()
"""

