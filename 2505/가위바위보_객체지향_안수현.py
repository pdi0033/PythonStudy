import random

class RockScissorPaper:
    rspList = ["", "가위", "바위", "보"]
    whoList = ["", "컴퓨터승", "사람승", "무승부"]
    gameList = []   # {computer: 값, person: 값, winner: 값}
    
    def isRsp(self, s):
        if s != "1" and s != "2" and s != "3":
            return False
        return True
    
    def isWinner(self, computer, person):
        if computer == person:  # 사람과 컴퓨터가 같다.
            return 3    # 무승부
        
        # 컴퓨터가 이기는 경우의 수 or
        # 가위-1, 바위-2, 보-3
        if (computer == 1 and person == 3) or \
            (computer == 2 and person == 1) or \
            (computer == 3 and person == 2):
            return 1    # 컴퓨터가 이김

        # 사람이 이기는 경우의 수 or
        if (computer == 1 and person == 2) or \
            (computer == 2 and person == 3) or \
            (computer == 3 and person == 1):
            return 2    # 사람이 이김
        
        return 0

    def output(self):
        computer_win = 0
        person_win = 0
        equal_win = 0
        for game in self.gameList:
            if game["winner"] == 1:
                computer_win += 1
            elif game["winner"] == 2:
                person_win += 1
            elif game["winner"] == 3:
                equal_win += 1

        for game in self.gameList:
            print(f"컴퓨터: {self.rspList[game["computer"]]},", end="\t")
            print(f"사람: {self.rspList[game["person"]]},", end="\t")
            print(f"승패: {self.whoList[game["winner"]]}")

        print(f"컴퓨터 승: {computer_win},\t사람 승: {person_win},\t무승부: {equal_win}")

    def gamePlay(self):
        self.gameList.clear()    # 데이터만 삭제
        print("게임을 새로 시작합니다.")
        # 계속 반복
        while True:
            computer = random.randint(1,3)
            person = input("1.가위, 2.바위, 3.보 >>")
            if self.isRsp(person) == False:
                continue

            person = int(person)
            winner = self.isWinner(computer, person)
            print(f"컴퓨터: {self.rspList[computer]}, 사람: {self.rspList[person]}, {self.whoList[winner]}")
            self.gameList.append({"computer": computer, "person": person, "winner": winner})

            again = input("게임을 계속 하시겠습니까? (y/n) >>")
            if again == "N" or again == "n":
                return

    def menuDisplay(self):
        print("1.게임시작")
        print("2.게임통계")
        print("0.게임종료")

    def gameStart(self):
        while True:
            self.menuDisplay()
            sel = input("입력 >>")
            
            if sel == "1":
                self.gamePlay()
            elif sel == "2":
                self.output()
            elif sel == "0":
                print("프로그램을 종료합니다.")
                return
            else:
                print("잘못 입력하셨습니다.")

if __name__ == "__main__":
    rsp = RockScissorPaper()
    rsp.gameStart()