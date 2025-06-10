# 거스름돈으로 줄 수 있는 동전이 [500원, 100원, 50원, 10원]일 때,
# 거스름돈 금액 N원을 입력받아 동전의 최소 개수를 구하라.

class Greedy:
    def __init__(self):
        self.coin = [500, 100, 50, 10]

    def calcul(self):
        while True:
            try:
                money = int(input("돈을 넣으세요. >> "))
                if money < 0 or (money%10 != 0):
                    raise(Exception)
            except Exception:
                print("양의 정수이자 10의 배수를 입력하세요.")
                continue
            break
        money = int(money)
        # coinList = [0] * len(self.coin)
        for index, value in enumerate(self.coin):
            # coinList[index] = money // value
            print(f"{value}원: {money // value}개", end="   ")
            money %= value
        print()
            
    def start(self):
        funcList = [None, self.calcul]
        while True:
            print("-" * 30)
            print("1. 돈 넣기")
            print("0. 종료")
            try:
                sel = int(input("입력 >> "))
                if sel < 0 or sel > len(funcList)-1:
                    raise(Exception)
            except Exception:
                print("제대로 입력하세요.")
                continue
            
            if sel == 0:
                return
            funcList[sel]()
            

if __name__ == "__main__":
    g = Greedy()
    g.start()