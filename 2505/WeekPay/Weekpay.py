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

if __name__ == "__main__":
    w1 = Weekpay("A")
    w1.output()