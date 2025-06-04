import pickle
from Drink import Drink

class Admin:
    def __init__(self):
        self.drinkList = []
        self.readDrinks()
        self.getIdPw()

    def readDrinks(self):
        with open("drinks.bin", "rb") as f:
            self.drinkList = pickle.load(f)

    def saveDrinks(self):
        with open("drinks.bin", "wb") as f:
            pickle.dump(self.drinkList, f)

    def getIdPw(self):
        with open("Admin.txt", 'r') as f:
            self.Id = f.readline().strip()
            self.Pw = f.readline().strip()
    
    def checkAdmin(self):
        print("Admin 계정의 ID와 PW를 입력하십시오.")
        for i in range(1,4):
            id = input("ID >>")
            pw = input("PW >>")
            if id == self.Id and pw == self.Pw:
                return True
            else:
                print(f"{i}번 틀리셨습니다.")
        return False

    def initDrinks(self):
        with open("drinks.txt", "r", encoding='utf-8') as f:
            self.drinkList.clear()
            data = f.readlines()

            # 재고들
            for d in data:
                dList = d.strip().split(',')
                name = dList[0]
                price = int(dList[1])
                inventory = int(dList[2])
                drink = Drink(name, price, inventory)
                self.drinkList.append(drink)
    
    def isInt(self, s):
        # 아무것도 입력 안 했을때
        if s == "":
            return False
        
        for i in s:
            if ord(i) < ord('0') or ord(i) > ord('9'):
                return False
        return True
    
    def isMenu(self, sel, round):
        # 정수가 아닐때
        if self.isInt(sel) == False:
            return -1
        sel = int(sel)
        # 범위가 아닐때
        if (sel < 0 or sel > round):
            return -1
        return 1
    
    def getInt(self, str="", round = 100, min = 0):
        while True:
            num = input(str)
            if self.isMenu(num, round) == -1:
                print("잘못 작성하셨습니다.")
                continue
            
            num = int(num)
            if num < min:
                print(f"{min} 이상 입력해주십시오.")
                continue
            if min == 10 and (num % 10 != 0):
                print("가격은 10의 단위로 입력해주십시오.")
                continue

            return num

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
    
    def restockDrink(self):
        while True:
            self.drinksDisplay()
            str = "어떤 상품을 채우시겠습니까?(번호로) >>"
            sel = self.getInt(round=len(self.drinkList), str=str)

            if sel == 0:    # 떠나기
                return
            
            str = f"{self.drinkList[sel-1].name}을 몇 개로 적재하시겠습니까?(최대 100개) >>"
            num = self.getInt(min=1, round=100, str=str)
                
            self.drinkList[sel-1].inventory = num
            

    def changePrice(self):
        while True:
            self.drinksDisplay()
            str = "어떤 상품의 가격을 바꾸시겠습니까?(번호로) >>"
            sel = self.getInt(round=len(self.drinkList), str=str)

            if sel == 0:    # 떠나기
                return
            
            str = f"{self.drinkList[sel-1].name}의 가격을 몇으로 정하시겠습니까?(최대 3만원) >>"
            num = self.getInt(min=10, round=30000, str=str)
            
            self.drinkList[sel-1].price = num

    def appenKind(self):
        name = ""
        while True:
            self.drinksDisplay()
            name = input("추가할 상품 이름 >>")
            name = name.strip()

            # 이미 있는 상품인지
            isAlready = False
            for drink in self.drinkList:
                if name == drink.name:
                    print("이미 존재하는 상품입니다.")
                    isAlready = True
                    break
            if isAlready == True:
                continue
            break
        
        str = "가격(최대 3만원) >>"
        price = self.getInt(min=10, round=30000, str=str)

        str = "재고(최대 100) >>"
        inventory = self.getInt(min=1, round=100, str=str)

        drink = Drink(name, price, inventory)
        self.drinkList.append(drink)


    def setIdPw(self, init=False):
        Id = "admin"
        Pw = "1234"
        if init == False:
            Id = input("ID >>")
            Pw = input("PW >>")

        with open("Admin.txt", "w") as f:
            print(Id, file=f)
            print(Pw, file=f)

    def initAll(self):
        self.initDrinks()
        self.setIdPw(init=True)

    def menuDisplay(self):
        print("-" * 15)
        print(" " * 3, "Admin", " " * 3)
        print("-" * 15)
        print("[0]  그만하기")
        print("[1]  재고 채우기")
        print("[2]  가격 변경")
        print("[3]  종류 추가")
        print("[4]  ID와 PW 변경")
        print("[5]  모두 초기화")

    def start(self):
        # 먼저 아이디와 비밀번호를 물어서 admin이 맞는지 확인
        if self.checkAdmin() == False:
            print("로그인 실패")
            return
        else:
            print("로그인 성공")
        
        while True:
            funcList = [self.saveDrinks, self.restockDrink, self.changePrice, self.appenKind, self.setIdPw, self.initAll]
            self.menuDisplay()
            str = "선택 >>"
            sel = self.getInt(round=(len(funcList)-1), str=str)
            
            sel = int(sel)
            funcList[sel]()
            if sel == 0:
                return

if __name__ == "__main__":
    a = Admin()
    a.start()