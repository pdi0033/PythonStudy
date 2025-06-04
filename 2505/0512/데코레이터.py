import time

# @staticmethod처럼 @로 시작한다.

def decorator1(func):   # 매개변수는 중첩함수 안에서 호출될 함수
    def wrapper():
        print("함수호출 전")
        func()
        print("함수호출 후")
    return wrapper  # 중첩함수의 참조를 반환해야 한다.

@decorator1
def hello():
    print("Hello")

hello()     # 함수호출 전 - Hello - 함수호출 후
# decorator1에게 납치당함 -> wrapper -> func()를 통해 함수호출


def time_decorator(callback):
    def innerfunction():
        start = time.time()
        callback()
        end = time.time()
        print(f"{callback.__name__} 실행시간: {end-start}초")
    return innerfunction

@time_decorator
def sigma():
    s = 1
    for i in range(1, 10000000):
        s += i
    print(f"합계: {s}")

sigma()

# 매개 변수 있고 반환값 있는 경우의 데코레이터 만들기
def mydecorator(callback):
    # 호출될 함수가 어떤 매개변수를 갖고 있는지 알 수 없을 경우에
    # tuple 타입, dict 타입 매개변수 하나
    def wrapper(*args, **kwargs):
        result = callback(*args, **kwargs)
        return result
    return wrapper

@mydecorator
def add(x,y):
    return x+y

print(add(5,7))

# 데코레이터 만들기 문제
# @mylog
# 함수를 sigma 매개변수 s = sigma2(10)
# [LOG] 함수이름: sigma2
# [LOG] 입력값: args = (10), kargs = {}
# [LOG] 반환값: 55
def myLog(callback):
    def wrapper(*args, **kargs):
        result = callback(*args, **kargs)
        # __name__은 내장 변수라 한다.
        print(f"[LOG] 함수이름: {callback.__name__}")
        print(f"[LOG] 입력값: args = {args}, kargs = {kargs}")
        print(f"[LOG] 반환값: {result}")
        return result       # 이거 안 하면 반환값이 전달 안 된다.
    return wrapper

@myLog
def sigma2(limit=10):
    sum = 0
    for i in range(1,limit+1):
        sum += i
    return sum

print(sigma2(100))
print(sigma2(10))

@myLog
def sub(a, b):
    return a-b
print(sub(3,4))