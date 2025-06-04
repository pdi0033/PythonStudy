# 가변매개변수
# 매개변수에 기본값을 줄 때는 변수 자체가 여러 개 만들어진다.
def myAdd(*args):   # 변수 하나에 값을 여러 개 전달한다.
    print(type(args))   # 튜플 타입. *args - tuple로 전달하겠다.
    for a in args:
        print(a)

myAdd(1,2)
myAdd("A",1)

def myAdd2(*data):
    s = 0
    for i in data:
        s += i
    return s

print( myAdd2(1,3,5) )
print( myAdd2(1,3,5,7,9) )
print( myAdd2(1,3,5,10,12,13) )

def myAdd3(n, *data):
    print("n", n)
    for i in data:
        print(i)

myAdd3(1,2,3,4,5)

# dict타입으로 매개변수 넘기기
# 매개변수 전달 방식이 달라진다.
def myFunc(d):
    print(d)

person = {"name": "홍길동", "age": 12}
myFunc(person)


def myFunc2(**d):
    print(d)

myFunc2(name="홍길동", age=23)

# 일반인자, 튜플인자, 딕인자
def profile(role, *skills, **details):
    print("Role", role)
    print("Skills", skills)
    print("Details", details)

profile("programmer", "python", "react", "deepLearning", 
        yearPay=100000000, position="개발자")

