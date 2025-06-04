"""
은행에 가면 순번 뽑기
1. 은행원 - 작업완료 -> 몇 번 손님 나오세요
2. 고객 번호뽑기 -> 대기인원
"""
from 큐1 import MyQueue

class BankNumber:
    def __init__(self):
        self.number = 0
        self.cnt = 0
        self.queue = MyQueue(500)
    
    def menuCustomer(self):
        self.number += 1
        self.cnt += 1
        self.queue.put(self.number)
        print(f"대기인원: {self.cnt}")
        print(f"고객님 번호는 {self.number} 입니다.")
    
    def menuBanker(self):
        # 큐에서 번호 하나를 꺼낸다.
        if self.queue.isEmpty():
            return 
        number = self.queue.get()
        print(f"{number} 고객님 창구 앞으로 와주세요.")
        self.cnt -= 1
        print(f"대기 인원: {self.cnt}")

    def main(self):
        while True:
            print("-" * 20)
            sel = input("1. 고객, 2. 은행원, 3. 종료 >> ")
            if sel == "1":
                self.menuCustomer()
            elif sel == "2":
                self.menuBanker()
            elif sel == "3":
                return
            else:
                print ("제대로 입력하십시오.")


if __name__ == "__main__":
    bm = BankNumber()
    bm.main()
        

    

