from GameData import Baseball

class GameMain:
    def __init__(self):
        self.gameList = []
        
    def gameStart(self):
        b = Baseball()
        b.start()
        self.gameList.append(b)

    def showStatistics(self):
        for b in self.gameList:
            print("-------------------------")
            print(f"컴퓨터: {b.computer}")
            for item in b.personList:
                print(f"사람: {item["person"]}, strike: {item["strike"]}, ball: {item["ball"]}, out: {item["out"]}")
            print(b.count, "라운드를 진행하셨습니다.")

    def start(self):
        while True:
            print("1.게임시작")
            print("2.통계")
            print("0.종료")
            sel = input("선택: ")

            if sel == "1":
                self.gameStart()
            elif sel == "2":
                self.showStatistics()
            elif sel == "0":
                return
            else:
                print("잘못 선택하셨습니다.")

if __name__ == "__main__":
    g = GameMain()
    g.start()