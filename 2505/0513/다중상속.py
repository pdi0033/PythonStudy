class Flyable:
    def fly(self):
        print("날 수 있다.")
    def walk(self):
        print("두 다리로 걷는다.")
        
class Swimmable:
    def swim(Self):
        print("수영할 수 있다.")
    def walk(self):
        print("***두 다리로 걷는다.***")

class Duck(Swimmable, Flyable):
    def quack(self):
        print("꽥꽥")

d1 = Duck()
d1.fly()
d1.swim()
d1.quack()
d1.walk()


# 시스템이 제공하는 내장변수 중에 __mro__ 가 상속받은 관계정보가 있어서
# 이걸 따라서 적용한다.
print(Duck.__mro__)     # 클래스 멤버변수로 제공한다.