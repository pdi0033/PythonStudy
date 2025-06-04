# 문제1. 주급계산: 이름, 근무시간, 시간당급여액, 추가수당 :근무시간이 20시간을 초과하면 시간당 급여액에 50%를 가산한다.
# 이름   근무시간  시간당급여  기본금액   수당   총액
# 홍길동,  30,    10000,     300000,  50000, 350000

# 입력
name = input("이름: ")
work_time = ""
per_money = ""
while not work_time.isdigit() :
    work_time = input("근무 시간: ")
while not per_money.isdigit():
    per_money = input("시간당 급여액: ")
work_time = int(work_time)
per_money = int(per_money)

# 계산
base_money = per_money * work_time
bonus_money = 0
if work_time > 20:
    bonus_money = int( (work_time - 20) * per_money / 2)

total_money = base_money + bonus_money

# 출력
text = (
    f"이름: {name}, "
    f"근무시간: {work_time}, "
    f"시간당급여액: {per_money}, "
    f"기본금액: {base_money}, "
    f"추가수당: {bonus_money}, "
    f"총액: {total_money}"
)

print(text)