# 과제: 야구게임
# 0~9 중에 숫자 3개를 컴퓨터가 랜덤하게     3 7 9
# 0~9 중에 숫자 3개를 입력받는다.           1 4 5   안 맞으면 out 여기서 3out
# 0~9 중에 숫자 3개를 입력받는다.           3 2 6   1strike 2out
# 0~9 중에 숫자 3개를 입력받는다.           8 2 6   3out
# 0~9 중에 숫자 3개를 입력받는다.           3 9 7   1strike 2ball 숫자는 맞지만 위치가 다를 때
# 0~9 중에 숫자 3개를 입력받는다.           3 7 9   3strike
# 5번만에 맞췄습니다.
# 6번 넘어가면 "못 맞췄습니다."
# 이렇게 숫자 맞추기 게임을 하는 거다.
# 통계
# 3 4 5
# 사람의 입력 과정 다 보여주기
# 5번 만에 맞췄고 
# 마지막에 승률도 나와야 한다.  50% 이런식으로
import random

gameHistory = []    # 컴퓨터 히스토리, 플레이어 히스토리, 승패 저장

def menuDisplay():
    print("1.게임시작")
    print("2.통계보기")
    print("0.게임종료")

def isStrike(s, playerHistory, computerNum):
    s = s.strip()
    sList = s.split(" ")
    nList = []
    strike = 0
    ball = 0
    out = 0

    for n in sList:
        n = int(n)
        nList.append(n)
    
    for i in range(0, len(computerNum)):
        if computerNum[i] == nList[i]:
            strike += 1
        elif computerNum[i] in nList:
            ball += 1
        else:
            out += 1
    
    if strike > 0:
        print(f"{strike} Strike", end="\t")
    if ball > 0:
        print(f"{ball} Ball", end="\t")
    if out > 0:
        print(f"{out} Out", end="\t")
    print()

    playerHistory.append(nList)
    if strike == 3:
        return True
    else:
        return False
    

def winDisplay():
    winCount = 0
    for i in gameHistory:
        print(f"컴퓨터 숫자: {i["computer"]}")
        print("플레이어 히스토리")
        print(i["player"])
        if i["win"] == True:
            winCount += 1
            round = len(i["player"])
            print(f"--{round}만에 승리했습니다.--")
        else:
            print("--못 맞췄습니다.--")

    winPer = (winCount / len(gameHistory)) * 100
    print(f"총 승률: {winPer:.2f}%")

def is3Num(s):
    s = s.strip()
    nList = s.split(" ")
    if len(nList) != 3:
        return False
    
    for i in nList:
        if (ord(i) < ord('0')) or (ord(i) > ord('9')):
            return False
    
    return True

def baseballGame():
    playerHistory = []
    computerNum = []
    noDuplication = set()
    
    while True:
        n = random.randint(0,9)
        noDuplication.add(n)
        computerNum = list(noDuplication)
        if len(computerNum) >= 3:
            break
    # print(computerNum)

    find = -1
    round = 1
    while round <= 6:
        print("0~9 중에 중복되지 않는 숫자 3개를 입력하세요. 띄어쓰기로 구분합니다.")
        n = input("입력 >>")
        if not is3Num(n):
            print("잘못 입력하셨습니다.")
            continue

        find = isStrike(n, playerHistory, computerNum)
        if find == True:
            break
        
        round += 1

    if find != True:
        print("못 맞췄습니다.")
    else:
        print(f"{round}번만에 맞췄습니다.")
    
    gameDic = {"computer": computerNum, "player": playerHistory, "win": find}
    gameHistory.append(gameDic)
    
    return

def gameStart():
    while True:
        menuDisplay()
        select = input("입력 >>")
        if select == "1":
            baseballGame()
        elif select == "2":
            winDisplay()
        elif select == "0":
            print("프로그래밍을 종료합니다.")
            return
        else:
            print("잘못 입력하셨습니다.")
        print()     # 보기 예쁘게

gameStart()