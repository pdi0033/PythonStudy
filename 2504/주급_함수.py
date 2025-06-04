workerList = [
    {"name": "홍길동", "work_time": 30, "per_pay": 20000, "pay": 0},
    {"name": "김길동", "work_time": 20, "per_pay": 30000, "pay": 0},
    {"name": "고길동", "work_time": 50, "per_pay": 20000, "pay": 0}
]     # 공용변수로 존재해야 한다.

def append():   # 데이터 추가 함수
    worker = {}     # dict 타입 객체 생성
    worker["name"] = input("이름: ")
    worker["work_time"] = int(input("일한 시간: "))
    worker["per_pay"] = int(input("시간당 급여액: "))
    worker["pay"] = 0

    workerList.append(worker)   # 목록에 추가하기

def output():   # 출력
    for w in workerList:
        print(f"{w["name"]}", end="\t")
        print(f"{w["work_time"]}", end="\t")
        print(f"{w["per_pay"]}", end="\t")
        print(f"{w["pay"]}", end="\t")
        print() # 줄바꿈 코드

def process(worker):    # dict 가져와서 반환하는 방법, 매개변수로 값을 받아오면 외부로 전달은 안 된다.
    worker["pay"] = worker["work_time"] * worker["per_pay"]

def process_main():
    for w in workerList:
        process(w)

def main():
    while (True) :  
        print("1.추가")
        print("2.출력")
        print("3.계산")
        print("0.종료")
        sel = input("선택: ")
        if sel == "1":
            append()
        elif sel == "2":
            output()
        elif sel == "0":
            print("프로그램을 종료합니다.")
            return  # 함수 자체를 종료시킨다.
        elif sel == "3":
            process_main()
        else:
            print("잘못 선택하셨습니다.")
        
main()