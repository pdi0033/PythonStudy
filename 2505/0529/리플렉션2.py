class MyType:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def sub(self):
        return self.x - self.y
    
    def mul(self):
        return self.x * self.y
    
my = MyType()

import inspect
# 문제1. inspect 써서 변수 리스트 뽑기
var_fields = []
for name, value in inspect.getmembers(my):
    if not(inspect.ismethod(value) or inspect.isfunction(value)) \
    and not name.startswith("__"):
        var_fields.append(name)
# 강사님코드
var_fields = [name for name, value in inspect.getmembers(my)
              if not(inspect.ismethod(value) or inspect.isfunction(value)) 
              and not name.startswith("__")]
print(var_fields)

# 문제2. inspect 써서 함수 리스트 뽑기
fun_fields = []
for name, value in inspect.getmembers(my):
    if (inspect.ismethod(value) or inspect.isfunction(value)) \
    and (not name.startswith("__")):
        fun_fields.append(name)
# 강사님코드
fun_fields = [name for name, value in inspect.getmembers(my)
              if (inspect.ismethod(value) or inspect.isfunction(value)) 
              and not name.startswith("__")]
print(fun_fields)

# 문제3. setattr 써서 x에는 값 10, y에는 값 5. add,sub,mul
setattr(my, var_fields[0], 10)
setattr(my, var_fields[1], 5)
print(my.add(), my.sub(), my.mul())

# 문제4. getattr로 함수 주소 갖고 와서 호출하기
a = getattr(my, fun_fields[0])
b = getattr(my, fun_fields[1])
c = getattr(my, fun_fields[2])
print(a(), b(), c())