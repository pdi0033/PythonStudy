class Person:
    def __init__(self, name="", age=20):
        self.name = name    # 두 개의 필드가 있다.
        self.age  = age

    def greet(self):
        print(f"Hello {self.name}")

p = Person("Tom", 12)

# 클래스 내의 속성을 가져온다.
a = getattr(p, 'name')  # 특정 객체로부터 속성을 가져올 수 있다.
print(a)
print(dir(p))

# 필터링해서 사용자가 만든거만
fields = [x for x in dir(p) if not x.startswith("__")]
print(fields)

for field in fields:
    print(getattr(p, field))


import inspect      # 이 라이브러리가 각 요소가 함수인지 아닌지 확인가능
# 특정 객체안에 있는 모든 메서드와 변수들을 다 가져온다.
print(inspect.getmembers(p))
for item, value in inspect.getmembers(p):
    if inspect.ismethod(value) or inspect.isfunction(value):
        print("함수", item)
    else:
        print("변수", item)

#[ 출력변수 for 출력변수 in iterable if 조건식]
# 클래스로부터 변수이름만 추출하기
var_fields = [ name for name, value in inspect.getmembers(p)
              if not (inspect.ismethod(value) or inspect.isfunction(value))
                and not name.startswith("__")]
print(var_fields)

# 클래스로부터 함수이름만 추출하기
fun_fields = [ name for name, value in inspect.getmembers(p)
              if  (inspect.ismethod(value) or inspect.isfunction(value))
                and not name.startswith("__")]
print(fun_fields)

a = getattr(p, var_fields[0])
print(a)

a = getattr(p, var_fields[1])
print(a)

setattr(p, 'name', '홍길동')
setattr(p, 'age', '43')

print(p.name, p.age)


def add(x, y):      # 함수도 주소임, 파이썬은 변수들한테 주소 저장가능
    return x+y

a = add
print(a(5,6))

method = getattr(p, "greet")
method()


# 함수의 매개변수
params = inspect.signature(add)
print(params)
print(params.parameters)


