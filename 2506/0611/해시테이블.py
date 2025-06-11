"""
1. 해시 함수
school - 각 단어별로 unicode 만들고 더해서 총합 구하기
        파이썬에서 문자의 unicode는 ord('a')
"""
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

head = [Node() for _ in range(100)]

def setHash(key):
    total = 0
    for ch in key:
        total += ord(ch)
    """
    해시 테이블
    head[0] -> ("scool"|??) _> ( |None)
    head[1] -> ("rain"|??) _> ( |None)
    head[2] -> ("desk"|??) _> ("chair"|??) -> ( |None)
    """
    index = total%100
    node = head[index]
    while node.data != None:
        node = node.next
    node.data = key
    node.next = Node()

def getHash(key):
    total = 0
    for ch in key:
        total += ord(ch)
    
    index = total%100
    node = head[index]
    while node.data != key and node.data != None:
        node = node.next
    if node.data != key:
        return "찾을 수 없습니다."
    return f"{node.data}는 해시테이블 {index}번방에 있습니다."

def hashPrint():
    for i in range(0, 100):
        if head[i].data != None:
            print(i, head[i].data)

if __name__ == "__main__":
    setHash("a")
    setHash("korea")
    setHash("school")
    hashPrint()

    print(getHash("a"))
    print(getHash("abc"))
    print(getHash("korea"))
    print(getHash("school"))

