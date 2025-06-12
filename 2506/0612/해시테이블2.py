# 데이터 타입만
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):  # 기본 연산자 오버라이딩, 
                        # 객체를 print할 때 이 연산자를 overriding해주면 원하는 대로 출력을 해준다.
                        # 안하면 객체 주소값 출력
        return f"{self.data} {self.next}"

class HashTable:
    def __init__(self, cnt=10):
        self.cnt = cnt
        if self.cnt < 10:   # 10개보다 작으면 최소한 bucket 개수를 10개는 만들자
            self.cnt = 10
        self.bucketList = [None] * self.cnt
        # 앞에 완충장치용으로 노드를 미리 만들어서 붙여놓자
        self.bucketList = [ Node() for i in range(0,self.cnt) ]
        # for i in range(0, 5):
        #     print(self.bucketList[i])
    
    def getHash(self, key): # 해쉬함수 붙이기
        total = 0
        for k in key:
            total += ord(k)
        return total % self.cnt
    
    # 해쉬테이블 구성 함수 => 해쉬 테이블을 구축을 해야 검색을 빠르게
    # 처음에 해쉬테이블 구축시간이 많이 걸린다.
    # Mysql join 이 외부에서 inner join, outer join
    def createTable(self, dataList=None):  # 생성자에서 해도 되는데 코드가 길어질 것 같아서 함수를 별도로 제작
                                    # 생성자에서 호출하면 된다.
        # 외부에서 [("book"), ("school"), ("rain")] 값을 받아온다.
        for item in dataList:
            # 1.해시 값을 가져온다.
            key = self.getHash(item)
            #print(item, key)
            # 2. Node(key)를 만들어서 노드의 앞쪽에 붙인다
            bucket = Node(item)
            # 3. bucket을 헤드 쪽에 붙인다.
            bucket.next = self.bucketList[key].next
            self.bucketList[key].next = bucket

    def printList(self):
        for item in self.bucketList:
            trace = item.next
            while trace != None:
                print(trace.data, end=" => ")
                trace = trace.next
            print()
    
    def search(self, word=""):
        # 1. 키값부터 구한다.
        key = self.getHash(word)
        trace = self.bucketList[key].next
        find = False
        while trace != None and not find:
            if trace.data == word:
                find = True
            else:
                trace = trace.next
        if not find:
            print("Not found")
        else:
            print("found")

if __name__ == "__main__":
    hash = HashTable()
    hash.createTable([("school"), ("desk"), ("chair"), ("rain"), ("survey"), ("house"), ("home")
                      , ("doll"), ("python"), ("java"), ("html"), ("javascript")])
    hash.printList()
    hash.search("school")
    hash.search("SCHEDULE")


