class Base: #부모 클래스
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print("Base 생성자")

    def display(self):
        print(f"x={self.x}, y={self.y}")

    def add(self):
        return self.x+self.y
    
    def doubleX(self):
        return self.x*2
    
    def doubleY(self):
        return self.y*2


class Child1(Base): #Base 클래스를 상속받음
    def __init__(self, x=0, y=0, z=0):
        # super() - 부모 객체를 가져온다.
        super().__init__(x,y)
        # self.x=x
        # self.y=y
        self.z=z
        print("Child1 생성자")

    def display(self):
        # super() - 부모 클래스의 함수를 먼저 호출하고 내가 만든 코드를 붙이고자 할 때.
        # super().함수명()
        print(f"x={self.x}, y={self.y}, z={self.z}")

        return 


p = Base()
p.display()

p = Base(4,5)
p.display()

c1 = Child1(1,2,3)
c1.display()
print(c1.doubleX())
print(c1.doubleY())

