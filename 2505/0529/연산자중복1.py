class MyType:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # self: 클래스 메서드들은 객체 자신에 대한 참조로 누구나 self를 가져야 한다.
    # other 전달받은 매개변수
    # 반환값이 객체여야 한다.
    def __add__(self, other):
        #print("***")
        result = MyType()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result
    
    # 반환값은 문자열이어야 한다.
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    
    # __sub__, __mul__, __truediv__
    def __sub__(self, other):
        # result = MyType()
        # result.x = self.x - other.x
        # result.y = self.y - other.y
        # return result
        return MyType(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return MyType(self.x * other.x, self.y * other.y)
    
    def __truediv__(self, other):
        # result = MyType()
        # result.x = self.x / other.x
        # result.y = self.y / other.y
        return MyType(self.x / other.x, self.y / other.y)
    

m1 = MyType(4,5)
m2 = MyType(8,9)
m3 = m1 + m2
print(m3)
print(str(m3))
# m3 = m1.__add__(m2) 
# result = m2 + m1
# m2.__add__(m1)

print(m1 - m2)
print(m1 * m2)
print(m1 / m2)


