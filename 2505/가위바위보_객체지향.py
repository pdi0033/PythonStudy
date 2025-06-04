 # 가위바위보 게임한판 - computer, person, 승부여부
import random

class GameData:
    # 변수 선언을 생성자에게 하자
    # 이유: 그래야 객체가 생성될 떄마다 새로운 메모리를 만드어준다.
    def __init__(self):
        self.computer = 0
        self.person = 0
        self.winner = 0

    def gameStart(self):
        self.computer = random.randint(1,3)
        self.person = int(input("1.가위, 2.바위, 3.보 >>"))
        self.winner = self.isWinner()

    def isWinner(self):
        s = self
        if s.computer == s.person:
            return 3    # 무승부
        elif (s.computer == 1 and s.person == 3) or \
        (s.computer == 2 and s.person == 1) or \
        (s.computer == 3 and s.person == 2):
            return 1    # 컴퓨터승
        # elif (s.computer == 1 and s.person == 2) or \
        # (s.computer == 2 and s.person == 3) or \
        # (s.computer == 3 and s.person == 1):
        return 2    # 사람승
    
    def printLog(self):
        print(f"컴퓨터: {self.computer}, 사람: {self.person}, 승부: {self.winner}")

class Game:
    titles1 = ["", "가위","바위","보"]
    titles2 = ["", "컴퓨터승", "사람승", "무승부"]

    def __init__(self):
        self.gameList = []  # game 정보를 저장한다.

    def printLog(self, g):
        print(f"컴퓨터: {self.titles1[g.computer]}", end="\t")
        print(f"사람: {self.titles1[g.person]}", end="\t")
        print(f"승부: {self.titles2[g.winner]}")

    def start(self):
        while True:
            g = GameData()
            g.gameStart()
            # g.printLog()
            self.printLog(g)
            self.gameList.append(g)

            again = input("1.계속, 0.종료 >>")
            if again != "1":
                return
        
    def printResult(self):
        print(f"{len(self.gameList)}번 수행함.")
        for g in self.gameList:
            self.printLog(g)
    
    def mainStart(self):
        self.start()
        self.printResult()

if __name__ == "__main__":  # 이 파일을 직접 main으로 실행할 때만 작동하도록 함. 모듈로 import할 때는 실행 안 됨.
    g = Game()  # 객체 생성
    g.mainStart()   # g->self로 전달된다.
    