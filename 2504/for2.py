# 1 ~ 10
# 변수 - 1 ~ 10 숫자 세는 변수
# 0 + 1
# 0 + 1 + 2
# 0 + 1 + 2 + 3
# 더해지는 값 - 누적값을 저장할 변수가 필요하다. 누적이 된다.
# for 문 밖에서 0으로 값을 초기화 되어야 한다.
sum = 0     # sum = sum + i
limit = int(input("limit: "))

for i in range(1,limit + 1):
    sum += i
    print(f"i={i} sum={sum}")



# list형 변수에 값 5개 넣어놓고 합계와 평균 구하기
#입력
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
list_num = []
for i in range(0,5):
    num = ""
    while not is_integer(num):
        if num != "":
            print("정수를 입력하세요!!!")
        num = input(f"{i+1} 번째 정수를 입력하세요: ")

    num = int(num)
    list_num.append(num)

# 계산
sum = 0
for i in list_num:
    sum += i

avg = sum / len(list_num)

# 출력
print(list_num)
print(f"총합: {sum}, 평균: {avg:.2f}")
