class Drink:
    def __init__(self, name="물", price = 1000, inventory = 10):
        self.name = name
        self.price = price
        self.inventory = inventory

    def output(self):
        print(f"{self.name}, {self.price}, {self.inventory}")

    def sell(self):
        if self.inventory <= 0:
            print("재고가 없습니다.")
            return False
        else:
            self.inventory -= 1
            return True

if __name__ == "__main__":
    d = Drink()
    d.output()
    d2 = Drink("콜라", 3000, 20)
    d2.output()
    print(d2.sell())
