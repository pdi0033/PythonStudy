# 성적처리
import random   # 외부 모듈(파이썬의 경우에는 파일)을 이 메모리로 가져와서 결합해라

# 전역 변수
# 모든 함수가 공유해야할 메모리다.
scoreList = list()      # scoreList = []

# 맨 처음에 기본 데이터 넣고 시작
def init():
    names = ["홍길동", "홍경래", "장길산", "강감찬", "서희", "윤관",
             "감강찬", "김연아", "안세영", "조승연"]
    for i in range(0, len(names)):
        scoreList.append({"name": f"{names[i]}",
                          "kor": random.randint(40, 100), 
                          "eng": random.randint(40, 100), 
                          "mat": random.randint(40, 100)})
    for score in scoreList:
        score["total"] = getTotal(score)
        score["avg"] = getAvg(score)
        score["grade"] = getGrade(score)

# ord 함수를 통해 숫자인지 0~9사이의 문자열인지 확인
def is_num(s):
    if s == "":
        return False
    for a in s:
        if ord(a) < ord('0') or ord(a) > ord('9'):
            return False
    return True

# 범위 내의 수인지 확인
def is_bound(s, bound = 100):
    s = int(s)
    if s < 0 or s > bound:
        return False
    return True

# 점수인지 확인
def is_score(s, bound = 100):
    if not is_num(s):
        return False
    if not is_bound(s, bound):
        return False
    return True

# 점수 입력
def get_score(s = "국어: ", bound = 100):
    subject = 0
    while True:
        subject = input(s)
        if not is_score(subject, bound):
            print(f"0 ~ {bound} 사이의 정수를 입력해주세요!")
            continue
        break

    return int(subject)

def getTotal(score):
    total = score["kor"] + score["eng"] + score["mat"]
    return total

def getAvg(score):
    avg = (score["kor"] + score["eng"] + score["mat"]) / 3
    return avg

def getGrade(score):
    if score["avg"] >= 90:
        return "수"
    elif score["avg"] >= 80:
        return "우"
    elif score["avg"] >= 70:
        return "미"
    elif score["avg"] >= 60:
        return "양"
    else:
        return "가"

# 데이터 세팅하기
def settingScore(score):
    # 각 과목별로 0~100점만 입력이 되도록
    # 숫자만 입력
    name = input("이름: ")
    kor = get_score("국어: ", 100)
    eng = get_score("영어: ", 100)
    mat = get_score("수학: ", 100)

    score["name"] = name
    score["kor"] = int(kor)
    score["eng"] = int(eng)
    score["mat"] = int(mat)
    score["total"] = getTotal(score)
    score["avg"] = getAvg(score)
    score["grade"] = getGrade(score)

# 1.입력
def append():
    score = {}
    settingScore(score)
    scoreList.append(score)
    
# 2.출력
def output(outList = scoreList):
    for score in outList:
        print(f"{score["name"]:6s}", end = "\t")
        print(f"{score["kor"]}", end = "\t")
        print(f"{score["eng"]}", end = "\t")
        print(f"{score["mat"]}", end = "\t")
        print(f"{score["total"]}", end = "\t")
        print(f"{score["avg"]:.2f}", end = "\t")
        print(f"{score["grade"]}")

# 3.검색
def search(allSame = False):
    word = input("이름을 입력하세요: ")
    # filter에서 두 번째 파라미터 iterable(반복적인) 데이터 - list류
    # filter 안에서는 scoreList로부터 한개씩 객체를 갖고 온다.
    if allSame == True:
        searchList = list( filter(lambda x: word == x["name"], scoreList) )
    else:
        searchList = list( filter(lambda x: word in x["name"], scoreList) )

    if len(searchList) == 0:
        print("검색된 이름이 없습니다.")
        return
    # 반환값이 list 타입이고 list안에 dict 타입이 있음
    # resultList, scoreList가 동일한 구조 - 함수 하나로 둘다
    # 함수 안에서 매개변수로 전역 변수와 이름이 똑같으면 외부 전역변수를 가려버린다.

    output(searchList)

    return searchList
    
# 4.수정
def modify():
    searchList = search(True)
    if searchList == None:
        return

    print("첫 번째만 수정합니다.")
    settingScore(searchList[0])

# 5.삭제
def delete():
    searchList = search(True)
    if searchList == None:
        return
    
    print("첫 번째만 삭제합니다.")
    scoreList.remove(searchList[0])


# 9. 랜덤 추가
def rand_append():
    name_words = "가나다라마바사아자차카타파하"
    name = ""
    for i in range(0, 3):
        n = random.randint(0, len(name_words)-1)
        name += name_words[n]

    scoreList.append({"name": f"{name}",
                    "kor": random.randint(40, 100), 
                      "eng": random.randint(40, 100), 
                      "mat": random.randint(40, 100)})
    for score in scoreList:
        score["total"] = getTotal(score)
        score["avg"] = getAvg(score)
        score["grade"] = getGrade(score)

def menuDisplay():
    print("1.추가")
    print("2.출력")
    print("3.검색")
    print("4.수정")
    print("5.삭제")
    print("9.랜덤 추가")
    print("0.종료")

def start():
    init()
    while (True) :  
        menuDisplay()
        sel = input("선택: ")

        if sel == "1":
            append()
        elif sel == "2":
            output()
        elif sel == "3":
            search()
        elif sel == "4":
            modify()
        elif sel == "5":
            delete()
        elif sel == "9":
            rand_append()
        elif sel == "0":
            print("프로그램을 종료합니다.")
            return  # 함수 자체를 종료시킨다.
        else:
            print("잘못 선택하셨습니다.")
        
        print()
        
start()