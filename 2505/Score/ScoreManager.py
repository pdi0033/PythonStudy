# ScoreData.py 파일에서 ScoreData 클래스를 가져와라
from ScoreData import ScoreData 
import pickle

class ScoreManager:
    def __init__(self):
        self.scoreList = [
            # ScoreData(),
            # ScoreData("조승연", 90, 80, 90),
            # ScoreData("안세영", 80, 80, 70),
            # ScoreData("김연경", 90, 90, 90),
            # ScoreData("김연아", 100, 80, 100)
        ]

    def printAll(self):
        for s in self.scoreList:
            s.print()

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
        sc = ScoreData()    #객체 생성
        sc.name = input("이름: ")
        sc.kor = int(input("국어: "))
        sc.eng = int(input("영어: "))
        sc.mat = int(input("수학: "))
        sc.process()
        self.scoreList.append(sc)

    def search(self):
        name = input("검색할 학생 이름: ")
        # filter는 두번째 매개변수로 전달된 list를 받아서
        # for문 돌려서 첫 번쨰 매개변수로 전달된 함수를 호출
        # 람다: 매개변수 하나 (scoreList에 저장된 객체 하나)
        #       반환은 True 또는 False
        # 매개 변수 ScoreData 객체
        # 전체 실행하는게 아니라 실행준비상태임 for를 사용하거나 list로 둘러 쌓으면 list생성자가 호출되면서 filter가 모든 작업을 완료한다.
        resultList = list(filter(lambda item: name in item.name, self.scoreList))
        # for sc in resultList:
        #     sc.print()

        # 데이터가 없을 경우에 처리 len(resultList)
        if len(resultList) == 0:
            print("찾으시는 데이터가 없습니다.")
            return
        
        for i, s in enumerate(resultList):
            print(f"[{i}]", end=" ")
            s.print()


    def modify(self):
        name = input("수정할 학생 이름: ")
        resultList = list(filter(lambda item: name in item.name, self.scoreList))

        if len(resultList) == 0:
            print("찾으시는 데이터가 없습니다.")
            return
            
        for i, sc in enumerate(resultList):
            print(f"[{i}]", end=" ")
            sc.print()

        sel = int(input("수정할 대상은(번호) >>"))
        # 수정할 대상의 참조를 가져온다.
        item = resultList[sel]
        item.name = input("이름: ")
        item.kor = int(input("국어: "))
        item.eng = int(input("영어: "))
        item.mat = int(input("수학: "))
        item.process()

    def delete(self):
        name = input("삭제할 학생 이름: ")
        resultList = list(filter(lambda item: name in item.name, self.scoreList))

        if len(resultList) == 0:
            print("찾으시는 데이터가 없습니다.")
            return
        
        for i, sc in enumerate(resultList):
            print(f"[{i}]", end=" ")
            sc.print()

        sel = int(input("삭제할 대상은(번호) >>"))
        # remove 객체 참조를 직접 부여한다.
        # 그 객체를 찾아서 삭제
        self.scoreList.remove(resultList[sel])

    def sort(self):
        # 원본 냅두고 정렬만 표기
        # key에 전달해야할 람다는 매개변수 하나
        # 반화값 정렬을 할 수 있는 데이터타입
        # < > 연산자가 가능한
        resultList = sorted(self.scoreList, key=lambda item: item.total, reverse=True)
        for i in resultList:
            i.print()


    def start(self):
        # 함수 주소를 배열에 저장하고 호출함
        funcList = [None, self.append, self.printAll, self.search, self.modify, self.delete, self.sort,
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

    def saveBinary(self):
        #직렬화
        with open("data.bin", "wb") as f:
            pickle.dump(self.scoreList, f)

    def readBinary(self):
        #역직렬화
        with open("data.bin", "rb") as f:
            self.scoreList = pickle.load(f)
        self.printAll()


if __name__ == "__main__":
    sm = ScoreManager()
    sm.start()