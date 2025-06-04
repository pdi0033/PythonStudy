# 숫자를 10 입력 받아서 각각 짝수, 홀수의 합과 평균을 구하는 프로그램을 작성하기
# 정수인지 확인하는 함수
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
# 입력
num = ""
num_list = []

for i in range(0,10):
    num = ""
    while not is_integer(num):
        if num != "":
            print("정수를 입력하세요!!!")
        num = input(f"{i+1} 번째 정수를 입력하세요: ")

    num = int(num)
    num_list.append(num)


# 계산
even_sum = 0
even_count =0
odd_sum = 0
odd_count =0
for item in num_list:
    if item % 2 == 0:
        even_sum += item
        even_count += 1
    else:
        odd_sum += item
        odd_count += 1

even_avg = even_sum / even_count
odd_avg = odd_sum / odd_count

# 출력
print(num_list)
print(f"짝수의 총합: {even_sum}, 짝수의 평균: {even_avg:.2f}")
print(f"홀수의 총합: {odd_sum}, 홀수의 평균: {odd_avg:.2f}")

