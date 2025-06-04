# 사칙연산을 하는 클래스를 만들어 보자
#공통위 데이터 공간을 두고
class Calculator:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y
    
    def sub(self):
        return self.x - self.y
    
c1 = Calculator(4,5)
print(c1.add())
print(c1.sub())

class Calculator2:
    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x - y
    
c1 = Calculator2()
print(c1.add(4,5))
print(c1.sub(4,5))

class Calculator3:  # 자바: 어노테이션
    @staticmethod   # 데코레이터
    def add(x, y):
        return x+y
    
    @staticmethod
    def sub(x, y):
        return x-y
    
    # cls를 사용하던 말던 매개변수로 전달은 반드시 필요하다.
    @classmethod
    def mul(cls, x, y):
        return x*y
    
print(Calculator3.add(4,5))
print(Calculator3.sub(4,5))
print(Calculator3.mul(4,5))