#모듈 Weekpay.py 파일에 있는 클래스 Weekpay 를 가져오겠다.
from Weekpay import Weekpay #외부파일(모듈을) 이 파일로 불러오기 
import pickle

# weekpay에 저장, 불러오기
# 연장 수당 20시간 넘으면 50% 추가

class Weekpay:
    def __init__(self, name="", work_time=20, per_pay=10000):
        self.name = name 
        self.work_time=work_time
        self.per_pay=per_pay
        self.bonus_pay = 0
        self.process() #클래스 내부 함수 호출시 self로 해야 한다 

    def process(self):
        self.pay = self.work_time * self.per_pay
        if self.work_time > 20:
            self.bonus_pay = self.per_pay * (self.work_time - 20) * 0.5
            self.pay += self.bonus_pay

    def output(self):
        print(f"이름: {self.name},\t근무시간: {self.work_time},\t시간당 수당: {self.per_pay},\t주급(추가수당 포함): {self.pay},\t추가 수당: {self.bonus_pay}")

class WeekPayManager:
    
    def __init__(self):
        self.wList = [
            # Weekpay("홍길동", 20, 20000),
            # Weekpay("고길동", 10, 50000),
            # Weekpay("김길동", 30, 40000),
            # Weekpay("이길동", 40, 20000),
            # Weekpay("장길동", 20, 20000)
        ]

    def output(self):
        for w in self.wList:
            w.output()

    def search(self):
        name = input("찾을 이름: ")
        resultList = list(filter(lambda w: name in w.name, self.wList))
        if len(resultList) == 0:
            print("데이터가 없습니다.")
            return
        
        #enumerate 함수는 인덱스랑, 데이터를 한꺼번에 반환한다.
        #resultList[0].ouput() #Weekpay의 output
        for w in resultList:
            w.output()
    
    def modify(self):
        name = input("찾을 이름: ")
        resultList = list(filter(lambda w: name in w.name, self.wList))
        if len(resultList) == 0:
            print("데이터가 없습니다.")
            return
        
        #enumerate 함수는 인덱스랑, 데이터를 한꺼번에 반환한다.
        #resultList[0].ouput() #Weekpay의 output
        for i, w in enumerate(resultList):
            print(i, end="\t")
            w.output()
        
        sel = int(input("수정할 대상을 입력하세요(숫자로) >>"))
        temp = resultList[sel]
        temp.name = input("이름: ")
        temp.work_time = int(input("근무시간 >>"))
        temp.per_pay = int(input("시간당급여액 >>"))
        temp.process()

    def saveBinary(self):
        #직렬화
        with open("C:/Users/PC/python_workspace1/2505/WeekPay/weekpay.bin", "wb") as f:
            pickle.dump(self.wList, f)

    def readBinary(self):
        #역직렬화
        with open("C:/Users/PC/python_workspace1/2505/WeekPay/weekpay.bin", "rb") as f:
            self.wList = pickle.load(f)
        self.output()

    def menuDisplay(self):
        print("--------------")
        print("     메 뉴     ")
        print("--------------")
        print("1.추가")
        print("2.출력")
        print("3.검색") # 이름
        print("4.수정") # 이름
        print("5.삭제") # 이름
        print("6.정렬") # 총점 내림차순
        print("7.파일로 저장")
        print("8.파일 불러오기")
        print("0.종료")
        print("--------------")

    def append(self):
        w = Weekpay()    #객체 생성
        w.name = input("이름: ")
        w.work_time = int(input("근무시간: "))
        w.per_pay = int(input("시간당 수당: "))
        w.process()
        self.wList.append(w)

    def delete(self):
        name = input("삭제할 사람 이름: ")
        resultList = list(filter(lambda w: name in w.name, self.wList))

        if len(resultList) == 0:
            print("데이터가 없습니다.")
            return
        
        #enumerate 함수는 인덱스랑, 데이터를 한꺼번에 반환한다.
        #resultList[0].ouput() #Weekpay의 output
        for i, w in enumerate(resultList):
            print(i, end="\t")
            w.output()

        sel = int(input("삭제할 대상은(번호) >>"))
        # remove 객체 참조를 직접 부여한다.
        # 그 객체를 찾아서 삭제
        self.wList.remove(resultList[sel])

    def sort(self):
        resultList = sorted(self.wList, key=lambda w: w.pay, reverse=True)
        for i in resultList:
            i.output()


    def start(self):
        # 함수 주소를 배열에 저장하고 호출함
        funcList = [None, self.append, self.output, self.search, self.modify, self.delete, self.sort,
                    self.saveBinary, self.readBinary]
        while True:
            self.menuDisplay()
            choice = int(input("선택: "))

            if choice > 0 and choice < len(funcList):
                funcList[choice]()
            elif choice == 0:
                return
            else:
                print("잘못된 메뉴입니다.")



mgr = WeekPayManager()
mgr.output()

if __name__ == "__main__":
    mgr = WeekPayManager()
    mgr.start()