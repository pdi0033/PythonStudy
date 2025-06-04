class MyQueue:
    def __init__(self, size=10):
        if size < 10:   #최소 10이상
            size=10
        self.size = size
        self.queue = [None] * self.size

        self.front = 0
        self.rear = 0

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def isFull(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

    def put(self, s=""):
        "rear 하나 증가시킨 다음에 % self.size로 나머지 구하고"
        "그 위치에 데이터 넣기"
        if self.isFull():
            print("가득 찬 상태입니다.")
            return False
        self.rear = (self.rear + 1) % self.size
        if s != "":
            self.queue[self.rear] = s
        else:
            self.queue[self.rear] = input("입력 >> ")
        return True

    def get(self):
        "front 증가시켜서 그 위치값 반환하기"
        if self.isEmpty():
            print("비어 있는 상태입니다.")
            return
        self.front = (self.front + 1) % self.size
        result = self.queue[self.front]
        self.queue[self.front] = None

        # print(f"{result} 번 손님 나오세요.")
        return result
    
    def peek(self):
        "front 자체는 바꾸면 안 된다."
        if self.isEmpty():
            print("비어 있는 상태입니다.")
            return
        temp = (self.front + 1) % self.size
        print(self.queue[temp])
        return self.queue[temp]

    def print(self):
        # print("표 상태")
        temp = self.front
        while temp != self.rear:
            temp = (temp+1)%self.size
            print(self.queue[temp], end='\t')
        print()

class Bank:
    def __init__(self):
        self.num = 1
        self.q = MyQueue()

    def start(self):
        while True:
            print("-" * 20)
            print("1. 은행원 - 작업완료")
            print("2. 고객 번호 뽑기")
            print("3. 전체 대기 인원")
            print("4. 다음 대기 번호")
            print("0. exit")
            sel = input("입력 >>")
            if sel == '0':
                break
            elif sel == '1':
                self.q.get()
            elif sel == '2':
                if self.q.put(self.num):
                    self.num += 1
                self.q.print()
            elif sel == '3':
                self.q.print()
            elif sel == '4':
                self.q.peek()


if __name__ == "__main__":
    b = Bank()
    b.start()
        
"""
은행에 가면 순번 뽑기
1. 은행원 - 작업완료 -> 몇 번 손님 나오세요
2. 고객 번호뽑기 -> 대기인원
"""
    

