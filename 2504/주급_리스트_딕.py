# 주급계산 이름, 근무시간, 시간당급여액 - 5명에 대해서
# 홍길동 40 10000
# 임꺽정 30 20000
# 장길산 20 30000
# 홍경래 10 15000
# 이징옥 20 30000

personList = [
    {"name": "홍길동", "work_time": 40, "per_pay": 10000},
    {"name": "임꺽정", "work_time": 30, "per_pay": 20000},
    {"name": "장길산", "work_time": 20, "per_pay": 30000}
]

for i in range(0,2):
    worker = {}
    worker["name"] = input("이름: ")
    worker["work_time"] = int(input("근무시간: "))
    worker["per_pay"] = int(input("시간당 급여액: "))
    personList.append(worker)

for worker in personList:
    worker["pay"] = worker["work_time"] * worker["per_pay"]

for worker in personList:
    print(f"{worker["name"]}  {worker["work_time"]}  {worker["per_pay"]} {worker["pay"]}")