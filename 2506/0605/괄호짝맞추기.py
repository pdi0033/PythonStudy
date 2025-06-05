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
            return False
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
            return False
        return self.stack[self.top]

    def pop(self):
        if self.isEmpty():
            return False
        item = self.stack[self.top]
        self.top -= 1
        return item
    
def checkBracket(arr):
    s = MyStack(len(arr))
    for a in arr:
        if a == "(":
            if s.push(a) == False:
                return False
        elif a == ")":
            if s.pop() == False:
                return False
    
    if s.isEmpty() == True:
        return True
    return False

if __name__ == "__main__":
    s1 = MyStack()
    
    print(checkBracket("((a*(b+c))-d) / e"))