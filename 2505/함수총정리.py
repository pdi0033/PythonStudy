global_x = 10   # 함수외부에 변수를 선언함
def myfunc1():
    # 함수 내부에서 변수에 값을 할당하는 순간 별도의 변수가 만들어진다.
    # 예외적으로 외부 변수를 같이 사용하고 싶다면 global을 앞에 붙인다.
    # 가능하다는 거지. 많이 쓰는 건 좋지 않다.
    global global_x
    global_x = 30   # 이 global_x는 지역변수다.
                    # 함수 내부에서만 존재하는 변수이다.
    y = 20
    print(global_x, y)

global_x = 100
myfunc1()
print(global_x)

# 함수의 매개변수 기본값
# dict로 받을 때도 호출하는 방식은 유사하다.

def myfunc2(name="홍기동", age=21, phone="010-0000-0001"):
    print(name)
    print(age)
    print(phone)

myfunc2()
myfunc2("임꺽정", 33)   # 필드 지정을 안 하면 차례대로 값이 부여된다.
myfunc2(name="둘리")
myfunc2(age=23)
myfunc2(phone="8-4833")

print(range(1,6))   # range라는 함수는 for문 안에서 호출하면 데이터 한개씩 만들어서 던져준다.
for i in range(1,6):
    print(i)

print()

def myrange(start=1, end=5):
    i = start
    while i<=end:
        yield i # 이 구문을 만나는 순간 값을 하나 반환하고 멈춘다.
        i += 1

gen = myrange() # 함수를 호출해서 저장해놓고 next를 통해서 호출한다.
# 이때 제너레이터 객체가 따로 만들어진다. 
# 내부적으로 파이썬이 일반함수를 제너레이터 객체로 만들어서 객체 참조를 gen한테 전달
# myrange(함수) => 제너레이터로 변환
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in myrange(1,10):
    print(i)

# 문제1
# 입력화면: 1.원의 면적, 2.사각형 면적, 3.사다리꼴 면적, 0.종료
# 1을 누르면
# 반지름: 5
# 면적은 78.5 입니다.
# 2를 누르면
# 가로: 5
# 세로: 7
# 면적은 35입니다.
# 사다리꼴은 아랫변, 윗변, 높이

def isNum(num):
    dotCount = 0
    for i in num:
        if ord(i) != ord('.') and (ord(i) < ord('0') or ord(i) > ord('9')):
            return False
        if ord(i) == ord('.'):
            dotCount += 1
            if dotCount >= 2:
                return False
    return True

def circleArea():
    while True:
        radius = input("반지름 >>")
        if isNum(radius) == False:
            print("숫자를 입력해주세요.")
            continue
        break
    
    radius = float(radius)
    area = radius * radius * 3.1415926535897932384626
    print(f"면적은 {area:.2f}입니다.")
        

def quadArea():
    while True:
        width = input("가로 >>")
        if isNum(width) == False:
            print("숫자를 입력해주세요.")
            continue
        break

    while True:
        heigth = input("세로 >>")
        if isNum(heigth) == False:
            print("숫자를 입력해주세요.")
            continue
        break
    
    width = float(width)
    heigth = float(heigth)
    area = width * heigth
    print(f"면적은 {area:.2f}입니다.")

def trapezoidArea():
    while True:
        up = input("윗변 >>")
        if isNum(up) == False:
            print("숫자를 입력해주세요.")
            continue
        break

    while True:
        down = input("아랫변 >>")
        if isNum(down) == False:
            print("숫자를 입력해주세요.")
            continue
        break

    while True:
        heigth = input("높이 >>")
        if isNum(heigth) == False:
            print("숫자를 입력해주세요.")
            continue
        break
    
    up = float(up)
    down = float(down)
    heigth = float(heigth)
    area = (up + down) * heigth / 2
    print(f"면적은 {area:.2f}입니다.")

def areaCal():
    while True:
        print("1.원의 면적")
        print("2.사각형 면적")
        print("3.사다리꼴 면적")
        print("0.종료")
        
        sel = input("입력 >>")
        if sel == "1":
            circleArea()
        elif sel == "2":
            quadArea()
        elif sel == "3":
            trapezoidArea()
        elif sel == "0":
            print("프로그램을 종료합니다.")
            return
        else:
            print("잘못 입력하셨습니다.")

    
def main2():
    myfunctions = {"1": circleArea, "2": quadArea, "3": trapezoidArea}
    while True:
        print("1.원의 면적")
        print("2.사각형 면적")
        print("3.사다리꼴 면적")
        print("0.종료")

        sel = input("입력 >> ")
        if sel in myfunctions.keys():
            myfunctions[sel]()  # 함수호출
        else:
            return
        
# main2()

# 문제2. 리스트를 받아가서 리스트 안에 중복된 데이터를 제거하고 중복되지 않는 데이터 리스트만 반환하기
def noDupliList(aList):
    newList = list()
    for i in aList:
        if not i in newList:
            newList.append(i)
    return newList

aList = [1,2,4,4,5,2,3,4,1]
print(noDupliList(aList))

# 문제3. myint 함수 문자열을 받아가서 정수로 바꾸어서 반환하기.
# "123"을 넣었을 경우에는 123을 반환. "123A"처럼 잘못된 데이터를 입력하면 -1을 반환하자.
def myint(num):
    for i in num:
        if ord(i) < ord('0') or ord(i) > ord('9'):
            return -1
    return int(num)

print(myint("123"))
print(myint("123A"))