def toDouble(x):
    x = x * 2

a = 10
toDouble(a)
print(a)

# a라는 변수와 함수의 매개변수는인 x는 서로 다른 공간이다.
# x라는 변수에 값을 복사해가고 함수 수행하면서 복사된 x값은 수정된다.
# 그러나 함수 외부와는 아무런 관계도 없다. call by value 함수를 값 복사로 호출한다.
# dict 타입이랑 list 타입의 경우에는 함수 내부에서 값 변환이 가능하다.
# 함수에 dict이나 list는 주소를 전달하는 방식이다.

def toDouble2(mydic):
    mydic["x"] *= 2
    mydic["y"] *= 2

mydic = {"x": 1, "y": 2}
toDouble2(mydic)
print(mydic)


def myadd(x = 0, y = 0, z = 0):
    return x + y + z

result = myadd(1,2,3)
print(result)

print(myadd())
print(myadd(1))
print(myadd(1,2))
print(myadd(1,2,3))


def myFunction(a,b,c=0,d=0,e=0):
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}")
    return a+b+c+d+e

print(myFunction(4,5))

def sigma(limit=10):
    sum = 0
    for i in range(1,limit+1):
        sum += i
    return sum

print(sigma())
print(sigma(15))
print(sigma(100))
