import pickle
from Admin import Admin
from Drink import Drink

class VendingMachine:
    def __init__(self):
        self.drinkList = []
        self.readDrinksFirst()
        self.requested = False
        self.gotoAdmin = 1234

    # 음료 메뉴 보여주기 
    def drinksDisplay(self):
        print("-" * 15)
        print(" " * 3, "메 뉴", " " * 3)
        print("-" * 15)

        for i, drink in enumerate(self.drinkList):
            print(f"[{i+1}]  {drink.name:10s}\t {drink.price:5d}원", end='\t')
            if drink.inventory <= 0:
                print("*재고 없음*")
            else:
                print(f"{drink.inventory:2d}개 남음")
        print("[0]  그만하기")

    def menuDisplay(self):
        print("-" * 15)
        print(" " * 3, "자판기", " " * 3)
        print("-" * 15)
        print("[0]  떠나기")
        print("[1]  음료 구매")
        # print("[2]  재고 요청")

    # 음료 구매
    def sellDrinks(self):
        while True:
            self.drinksDisplay()
            sel = input("선택 >>")
            if self.isMenu(sel, len(self.drinkList)) == -1:
                print("잘못 선택하셨습니다.")
                continue

            sel = int(sel)
            if sel == 0:    # 떠나기
                return
            
            isSell = self.drinkList[sel-1].sell()
            if isSell == False:
                print("재고가 없습니다.")
                continue
                # admin을 만들면서 재고 채우기 기능은 그곳으로 옮김
                # 따라서 이건 사용하지 않음.
                if self.requested == False:
                    yn = input("재고가 없습니다. 재고를 요청하시겠습니까? (Y/N) >>")
                    yn = yn.upper()
                    if yn == "Y" or yn == "YES":
                        self.requestRestock()
                    continue
                elif self.requested == True:
                    print("재고는 내일 채워집니다.")
                    continue
            
            self.doPay(self.drinkList[sel-1])

    # 돈 계산
    def doPay(self, drink):
        remainPrice = self.pay(drink)

        if remainPrice == 0:
            return
        # 나온 거스름돈은 음수라 양수로 만들기
        remainPrice *= -1

        self.change(remainPrice)

    # 돈 넣기
    def pay(self, drink):
        priceDic = {"5만원": 50000, "1만원": 10000, "5천원": 5000, "1천원": 1000,
                    "500원": 500, "100원": 100, "50원": 50, "10원": 10}
        print("-" * 15)
        print("돈을 넣습니다.")
        remainPrice = drink.price
        while remainPrice > 0:
            print("-" * 15)
            print(f"남은 돈: {remainPrice}원")
            for i, key in enumerate(priceDic.keys()):
                print(f"[{i}]  {key}")

            sel = input("선택 >>")
            if self.isMenu(sel, len(priceDic)-1) == -1:
                print("잘못 선택하셨습니다.")
                continue
            
            sel = int(sel)
            keyList = list(priceDic.keys())
            remainPrice -= priceDic[keyList[sel]]
        
        return remainPrice


    # 거스름돈
    def change(self, remainPrice):
        priceDic = {"5만원": 50000, "1만원": 10000, "5천원": 5000, "1천원": 1000,
                    "500원": 500, "100원": 100, "50원": 50, "10원": 10}
        print("-" * 15)
        print("거스름돈을 드립니다.")
        changeDic = {}

        while remainPrice > 0:
            for key, value in priceDic.items():
                if remainPrice >= value:
                    if key not in changeDic.keys():
                        changeDic[key] = 1
                    else:
                        changeDic[key] += 1

                    remainPrice -= value
                    break

        for key, value in changeDic.items():
            print(f"{key}  {value}개")

    # 재고 요청
    def requestRestock(self):
        with open("restock.txt", "w") as f:
            print("Restock Yes",file=f)
        print("다음 날에 전부 채워집니다.")
        self.requested = True

    def isInt(self, s):
        # 아무것도 입력 안 했을때
        if s == "":
            return False
        
        for i in s:
            if ord(i) < ord('0') or ord(i) > ord('9'):
                return False
        return True
    
    def isMenu(self, sel, round, checkAdmin=False):
        # 정수가 아닐때
        if self.isInt(sel) == False:
            return -1
        sel = int(sel)
        # 범위가 아닐때
        if (sel < 0 or sel > round):
            if checkAdmin == False:
                return -1
            elif checkAdmin == True and sel == self.gotoAdmin:
                return 3
        return 1

    def start(self):
        while True:
            funcList = [self.saveDrinks, self.sellDrinks] #, self.requestRestock]
            self.menuDisplay()
            sel = input("선택 >>")
            if self.isMenu(sel, len(funcList)-1, checkAdmin=True) == -1:
                print("잘못 선택하셨습니다.")
                continue
            elif self.isMenu(sel, len(funcList)-1, checkAdmin=True) == 3:
                # 어드민 계정
                admin = Admin()
                admin.start()
                self.readDrinks()
                continue
            
            sel = int(sel)
            funcList[sel]()
            if sel == 0:
                return

    def readDrinksFirst(self):
        # admin 클래스를 만들며 재고 채우기 기능은 그곳으로 옮김
        """
        # 재고를 채울지 확인할 변수
        fRestock = open("restock.txt", "r")
        self.restock = fRestock.readline().strip()
        fRestock.close()

        if self.restock == "Restock Yes":       # 재고를 채워야 한다면.
            with open("drinks.txt", "r", encoding='utf-8') as f:
                data = f.readlines()

                # 재고들
                for d in data:
                    dList = d.strip().split(',')
                    name = dList[0]
                    price = int(dList[1])
                    inventory = int(dList[2])
                    drink = Drink(name, price, inventory)
                    self.drinkList.append(drink)
                
                # 채웠다고 알리기
                with open("restock.txt", "w") as fRestock:
                    print("Restock No",file=fRestock)
        else:
        """
        self.readDrinks()
    
    def saveDrinks(self):
        with open("drinks.bin", "wb") as f:
            pickle.dump(self.drinkList, f)

    def readDrinks(self):
        with open("drinks.bin", "rb") as f:
            self.drinkList = pickle.load(f)

if __name__ =="__main__":
    vm = VendingMachine()
    vm.start()