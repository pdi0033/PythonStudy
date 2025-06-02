# 구조가 클래스나 구조체를 써야 한다.
class Node:
    def __init__(self, data=None):
        self.data = data    # 데이터파트
        self.next = Node    # 다음번 노드의 주소를 줘야 한다.

class MyList:
    # head와 tail
    # head - 리스트의 시작을 가리킨다.
    # tail - 리스트의 마지막을 가리킨다.
    def __init__(self):
        self.head = Node()      # 안씀. 자동차의 범퍼와 같은 역할
        self.tail = Node()      # 안씀. 자동차의 범퍼와 같은 역할
        self.head.next = self.tail
        self.tail.next = self.tail

    def insertHead(self, data):
        # 노드개체를 새로 생성한다.
        temp = Node(data)
        # 연결작업을 한다.
        temp.next = self.head.next  # 먼저해야 한다.
        self.head.next = temp

        # head->(|) ->            (|) -> tail
        #              temp->(|)->

    def print(self):
        print(self.head.next.data)
        print(self.head.next.next.data)
        print(self.head.next.next.next.data)

    def print2(self):
        # head의 값과 tail의 값은 절대 바뀌면 안 된다.
        # 추적용 Node 타입을 선언
        trace = self.head.next
        while trace != self.tail:
            print(trace.data)
            trace = trace.next

    def deleteHead(self):
        if self.head.next == self.tail:
            return      # 이미 다 삭제되어서 없음
        self.head.next = self.head.next.next

    def deleteAll(self):
        self.head.next = self.tail

    def insertOrder(self, data, myfunc=lambda x: x):
        temp = Node(data)
        # 1. 위치 찾기
        t1 = self.head.next
        t2 = self.head  # 뒤에서 따라감
        # 위치를 찾거나 마지막에 도달했을 때 끝내야 한다.
        flag = False    # while문을 종료하기 위한 조건
        while not flag and t1 != self.tail:
            if myfunc(t1.data) > myfunc(temp.data):
                flag = True     # 탐색을 중단
            else:
                t1 = t1.next
                t2 = t2.next
        
        # t2와 t1사이에 temp를 끼워넣는다.
        temp.next = t1
        t2.next = temp

m1 = MyList()
"""
m1.insertHead("A")
m1.insertHead("B")
m1.insertHead("C")
m1.print2()
print("-"*20)

m1.deleteHead()
m1.print2()
print("-"*20)
m1.deleteAll()
m1.print2()


m1.insertOrder("A")
m1.insertOrder("C")
m1.insertOrder("B")
m1.insertOrder("D")
m1.print2()
"""

class Book:
    def __init__(self, title="", author="", publisher=""):
        self.title = title
        self.author = author
        self.publisher = publisher

    def __gt__(self, other):    # > 연산자 중복
        if self.title > other.title:
            return True
        return False
    
    def __str__(self):
        return f"{self.title}, {self.author}, {self.publisher}"

print(Book("마법사의 돌", "조앤롤링", "해냄") >
      Book("마법사의 돌", "조앤롤링", "해냄"))
print(Book("마법사의 돌", "조앤롤링", "해냄") >
      Book("그리고 아무도 없었다.", "아가사 크리스티", "마르틴 프레스"))

m1.insertOrder(Book("마법사의 돌", "조앤롤링", "해냄"))
m1.insertOrder(Book("그리고 아무도 없었다.", "아가사 크리스티", "마르틴 프레스"))
m1.insertOrder(Book("구운몽", "김만중", "조선 중기"))
m1.print2()



