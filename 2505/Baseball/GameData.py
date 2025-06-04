import random
class Baseball:
    def __init__(self):
        self.computer = [-1, -1, -1]    # 아무값도 없다.
        self.person = [-1, -1, -1]      # 아무값도 없다.
        self.count = 0      # 몇 번 했는지
        self.personList = []

    def initComputer(self):
        cnt = 0 #랜덤값 3개 추출. 중복X
        while cnt < 3:
            v = random.randint(0,9)
            if v not in self.computer:  # 중복 아닐때
                self.computer[cnt] = v
                cnt += 1

    def initPerson(self):
        s = input("숫자 3개(0~9)를 입력하세요.(예시: 0 1 2) >>")
        # s.strip()
        # numberList = s.split(" ")
        numberList = s.strip().split(" ")     # 이것도 가능
        self.person[0] = int(numberList[0])
        self.person[1] = int(numberList[1])
        self.person[2] = int(numberList[2])

    def getResult(self):
        # 스트라이크, 볼, 아웃 개수
        strike = 0
        ball = 0
        out = 0

        for i in range(len(self.computer)):
            if self.person[i] == self.computer[i]:
                strike += 1
            elif self.person[i] in self.computer:
                ball += 1
            else:
                out += 1
        
        return strike, ball, out

    def start(self):
        # 3strike 이거나 5번의 기회를 다 사용했을 경우에 종료한다.
        self.count = 0
        flag = False    # 아직 3strike가 아님을 나타내기 위한 변수
        self.initComputer()
        print(self.computer)

        while (flag == False) and (self.count <= 5):
            self.initPerson()
            strike, ball, out = self.getResult()
            print(f"strike:{strike}, ball:{ball}, out:{out}")
            self.count += 1
            self.personList.append({"person": [x for x in self.person], 
                                    "strike": strike,
                                    "ball": ball,
                                    "out": out})

            if strike == 3:
                flag = True
                

if __name__ == "__main__":
    b = Baseball()
    b.start()