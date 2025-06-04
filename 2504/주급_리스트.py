# 주급계산 이름, 근무시간, 시간당급여액 - 5명에 대해서
# 홍길동 40 10000
# 임꺽정 30 20000
# 장길산 20 20000
# 홍경래 10 15000
# 이징옥 20 30000

# 입력
"""
names = ["홍길동", "임꺽정", "장길산", "홍경래", "이징옥"]
work_time = [40, 30, 20, 10, 20]
per_money = [10000, 20000, 20000, 15000, 30000]
"""
names = []
work_time = []
per_payList = []
payList = []

for i in range(0,5):
    name = input("이름: ")
    time = input("근무시간: ")
    per_pay = input("시간당급여액: ")

    names.append(name)
    work_time.append(int(time))
    per_payList.append(int(per_pay))

# 계산
for i in range(len(work_time)):
    pay = work_time[i] * per_payList[i]
    payList.append(pay)

# 출력
for i in range(len(names)):
    print(f"이름: {names[i]}, 근무시간: {work_time[i]}, 시간당급여액: {per_payList[i]}, 주급: {payList[i]}")
