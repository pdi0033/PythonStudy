class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None    # 앞의 노드 주소를 간직
        self.next = None    # 뒤의 노드 주소를 간직

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()      # 리스트 전체의 시작을 가리킨다.
        self.tail = Node()      # 리스트 전체의 끝을 가리킨다.
        self.head.next = self.tail
        self.tail.next = self.tail
        self.head.prev = self.head
        self.tail.prev = self.head
        # head <=> (|) <=> (|) <=> tail

    def insertHead(self, data=None):
        temp = Node(data)
        temp.next = self.head.next
        self.head.next.prev = temp
        self.head.next = temp
        temp.prev = self.head

        self.head.next = temp
        temp.prev = temp.next.prev
        temp.next.prev = temp


    def deleteTail(self):
        if self.tail.prev == self.head:
            return
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail


if __name__ == "__main__":
    pass













