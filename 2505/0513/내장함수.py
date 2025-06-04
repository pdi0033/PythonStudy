# 절대값 구하는 함수
print(abs(-4))
print(abs(4))

#지금 전달받은 요소 중에 0이 하나라도 존재하면 False
#요소 전체가 True이면 True
# 0, False, "" - Flase
print(all([]))          # True
print(all([1,2,3]))
print(all([1,2,3,0]))
print(all(["a","b",""]))
print("---------------------")

#지금 전달받은 요소 중에 0이 아닌 것이 하나라도 존재하면 True
# 요소 전체가 False이면 False
print(any([]))
print(any([1,2,3]))
print(any([1,2,3,0]))
print(any([0,0,0]))
print("---------------------")

#########################################################
# 내부함수를 확인
print(dir([1,2,3]))
print(dir(dict()))

# 몫과 나머지를 tuple로 보낸다.
mok, nmg = divmod(5,3)
print(mok)
print(nmg)

for i, c in enumerate("Life is egg"):
    print(i, c)

print("---------------------")
# 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값을 리턴하는 함수이다.
result = eval('1+10+3')
print(result)

result = eval('(1+10)*2-3')
print(result)

x1=1
x2=2
result = eval('x1 + x2')
print(result)

print("---------------------")
# 음수만 filter의 첫 번째 매개변수는 함수여야 한다.
# 두 번째 매개변수로 전달된 욧 하나를 매개변수로 하고 반환은
# True또는 False
a = [3,4,-1,2,9,8,7,12,15,21]
def isPositive(x):
    if x>0:
        return True
    return False

poList = list(filter(isPositive, a))
print(poList)

# 한번 만들어서 쓰고 버리는 함수인 람다를 사용하자
poList = list(filter(lambda x: x>0, a))
print(poList)

print("---------------------")
print(f"최대값 {max(a)}, 최소값 {min(a)}")
print(pow(2,4), 2**4)

# 반올림
print(round(4.5))   #4
print(round(4.2293))    #4
print(round(4.2293, 2)) #4.23


#컴퓨터는 시간을 1970년 1월 1일을 기준점으로 초당 1씩 카운트
import datetime
day1 = datetime.date(2021,12,14)
day2 = datetime.date(2023,4,5)
print(day1)
print(day2)
day3 = day2 - day1      # timedelta 객체로 바뀌고 날짜를 갖고 있다.
print(day3.days)

#말일까지 며칠이 남았는가?
day_end = datetime.date(2025,12,31) - datetime.date(2025,5,13)
print(day_end.days)
print("---------------------")

import calendar
from datetime import date
#오늘 날짜를 구한다.
today = date.today()
year = today.year
month = today.month

#tuple 해당월의 첫째날과 마지막 날
last_day = calendar.monthrange(year,month)[1]
print(last_day)
day1 = datetime.date(year, month, last_day)
print( (day1- today).days )

#오늘은 무슨 요일인지
print(today.weekday())
#date.weekday()는 0 1 2 3 4 5 6   >>   월 화 수 목 금 토 일
#문제. 날짜를 입력 받아서 그날이 무슨 요일인지 반환
#"2025-05-11"
def whatWeek():
    weekKor = ["월", "화", "수", "목", "금", "토", "일"]
    year, month, day = 0, 0, 0
    while True:
        inputDay = input("날짜를 입력해주세요.(예시. 2000-01-01)  >>")
        try:
            year, month, day = inputDay.strip().split('-')
            year = int(year)
            month = int(month)
            day = int(day)

            if year <= 0 or month <= 0 or day <= 0:
                raise Exception("년도, 월, 날은 0보다 커야 합니다.")
            if month > 12:
                raise Exception("월은 12보다 클 수 없습니다.")
            last_day = calendar.monthrange(year,month)[1]
            if day > last_day:
                raise Exception(f"{year}년 {month}월은 {last_day}보다 클 수 없습니다.")
        except Exception as e:
            print(f"{e}\n다시 입력해주세요.")
            continue

        break
    whatDay = datetime.date(year, month, day)
    print(f"{year}년 {month}월 {day}는 {weekKor[whatDay.weekday()]}요일 입니다.")

#whatWeek()

#강사님이 하신 거
day1 = datetime.datetime.strptime("2025-05-11", "%Y-%m-%d")
print(day1.weekday())

def getWeekDay(s):
    day1 = datetime.datetime.strptime(s, "%Y-%m-%d")
    weekday = day1.weekday()
    titles = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    return titles[weekday]

print(getWeekDay("2025-04-11"))

print("---------------------")

#딥러닝 때 shutil 사용함
import shutil
shutil.copy("./내장함수.py", "./내장함수2.py")

import glob
filelist = glob.glob("C:/*")
print(filelist)

filelist = glob.glob("./*.py")
print(filelist)

print("---------------------")
import os
#print(os.environ)
print(os.environ["PATH"])
print("---------------------")
print(os.getcwd())

#파이썬에서 OS명령어를 쓰고 싶을 때
os.system("dir/w")  #/w는 옆으로 보여줘라