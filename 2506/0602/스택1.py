class MyStack:
    def __init__(self, size=10):
        if size < 10:
            self.size = 10   # 최소 크기를 10으로 하자.
        else:
            self.size = size

        self.stack=[]
        for i in range(0, self.size):
            self.stack.append(0)
        self.top = -1

    # push 함수
    # isFull 상태가 아니면 top 증가시키고 그 안에 값 넣기
    def isFull(self):
        if self.size-1 == self.top:
            return True
        return False
    
    def push(self, data):
        if self.isFull():
            return
        self.top += 1
        self.stack[self.top] = data

    def print(self):
        i=0
        while i <= self.top:
            print(self.stack[i], end= " ")
            i += 1
        print()

    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[self.top]

    def pop(self):
        if self.isEmpty():
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item
    
def reverse1(arr):
    s = MyStack(len(arr))
    for i in arr:
        s.push(i)
    result = ""
    while not s.isEmpty():
        result += s.pop()
    return result

if __name__ == "__main__":
    s1 = MyStack()
    s1.push('A')
    s1.push('B')
    s1.push('C')
    s1.push('D')
    s1.push('E')
    s1.push('F')
    s1.push('G')
    s1.push('H')
    s1.push('I')
    s1.push('J')
    s1.push('K')
    s1.print()
    print("-------------------------------------")
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())

    # 스택을 사용해서 문자열 뒤집기 
    # reverse
    print(reverse1("korea"))