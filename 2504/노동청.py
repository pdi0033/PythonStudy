# 지방 노동청에 신고가 들어옴.
# 회사가 성별간 임금차별. 이거 현실이잖아ㅋㅋ
# 성별과 연봉
# 직원 전체 10명이고, 남자 평균, 여자 평균 구하기

# 입력
employeeList = []

for i in range(0,10):
    gender = input("성별: ")
    pay = int(input("임금: "))

    # employeeList.append( {"gender": gender, "pay": pay} )
    employee = {}
    employee["gender"] = gender
    employee["pay"] = pay
    employeeList.append(employee)

# 계산
male_pay = 0
female_pay = 0
male_count = 0
female_count = 0

for employee in employeeList:
    if employee["gender"] == "f" or employee["gender"] == "female" or employee["gender"] == "여자" or employee["gender"] == "여":
        female_pay += employee["pay"]
        female_count += 1
    else:
        male_pay += employee["pay"]
        male_count += 1

# 출력
if male_count > 0:
    print(f"남성 평균: {(male_pay / male_count):.2f}")

if female_count > 0:
    print(f"여성 평균: {(female_pay / female_count):.2f}")