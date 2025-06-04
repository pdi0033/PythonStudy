# 과제1. 정수를 받아가서 짝수이면 True 짝수가 아니면 False를 반환하는 함수
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input("정수를 입력하세요: "))
print(is_even(num))

# 과제2. 윤년 4년마다 윤년이다.
#       100년에 한 번씩 윤년이 아니다.
#       400년에 한 번씩 윤년이다.
#       함수를 만들어서 연도를 주면 윤년일 경우 True 윤년이 아니면 False를 반환
def is_leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

year = int(input("년도를 입력하세요: "))
print(is_leapYear(year))


def isEven(n):
    if n % 2 == 0:
        return True
    return False

def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

for i in range(1,11):
    print(f"{i} = {isEven(i)}")
print()

for i in range(2000, 2026):
    print(f"{i}년은 {isLeap(i)}")