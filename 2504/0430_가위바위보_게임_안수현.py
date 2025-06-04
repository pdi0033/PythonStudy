# 가위바위보 게임
# 컴퓨터가 1,2,3중에 랜덤값 하나를 생각하고 있음
# 사람이 1.가위 2.바위 3.보 입력
# 컴퓨터승 사람승 무승부 출력
# 게임 10번 해서 승률 출력까지
# 컴퓨터 3  사람 2  무승부 5
import random

RockScissorPaper = ["가위", "바위", "보"]
playerDict = {"Win": 0, "Draw": 0, "Lose": 0}

# 메뉴 보이기
def menuDisplay():
    print("1.게임하기")
    print("2.승률보기")
    print("0.종료")

# 이겼는지 비겼는지 졌는지 확인
def isWin(computer, player):
    print(f"플레이어: {RockScissorPaper[player-1]}, 컴퓨터: {RockScissorPaper[computer-1]}")
    if player == computer:
        playerDict["Draw"] += 1
        print("무승부")
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        playerDict["Lose"] += 1
        print("컴퓨터 승")
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        playerDict["Win"] += 1
        print("플레이어 승")
    print()

# 플레이하기
def gamePlay():
    while True:
        select = input("1.가위, 2.바위, 3.보 >>")
        if select != "1" and select != "2" and select != "3":
            print("잘못 입력하셨습니다.")
        else:
            break
    
    select = int(select)
    computer = random.randint(1,3)
    isWin(computer, select)
    

def winDisplay():
    print(f"컴퓨터: {playerDict["Lose"]}, 플레이어: {playerDict["Win"]}, 무승부: {playerDict["Draw"]}")
    print()

def start():    
    while True:
        menuDisplay()
        select = input(">>")
        if select == "1":
            # 게임하기
            gamePlay()
        elif select == "2":
            # 출력하기
            winDisplay()
        elif select == "0":
            print("게임을 종료합니다.")
            break
        else:
            print("잘못 입력하셨습니다.")

    print("end")

start()