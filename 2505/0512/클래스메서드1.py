class MyClass:
    # 클래스 변수의 영역이다.
    # 객체를 만들던 말던 한 번만 만든다.
    # 생성자에서 이 부분을 건드리면 안 된다.
    count=0     # 객체가 만들어질 때마다 몇 개 만들어졌는지 확인하고 싶다.
    @staticmethod
    def addCount():     # static 메서드 입장에서는 매개변수인 self를 사용 못하니까 cout 변수 접근불가
        count += 1

    @classmethod
    def increase(cls):  # cls는 클래스다.
        cls.count += 1

#print(MyClass.addCount())      # 에러

MyClass.increase()
print(MyClass.count)

# 객체를 만들 때 객체의 개수를 카운트하거나 제한하는 클래스를 만들고자 할 때 classmethod를 사용한다.

class SelfCount:
    # 변수에 __를 붙이면 외부에서 접근이 불가능하다
    __count = 0
    # 생성자에서 값 증가하기
    def __init__(self):
        SelfCount.__count += 1

    @classmethod
    def count_output(cls):
        print(cls.__count)


# print(SelfCount.__count)    # 이 속성을 볼 수 없다는 에러 메시지
s1 = SelfCount()
SelfCount.count_output()
s1 = SelfCount()
SelfCount.count_output()
s1 = SelfCount()
SelfCount.count_output()
s1 = SelfCount()
SelfCount.count_output()