# 정수를 입력받아
# 홀수의 합계와 짝수의 합계를 보여주자

even_sum = 0
odd_sum = 0

numberList = []     # 리스트 객체를 만든다.
# 1.입력
for i in range(0,4):
    num = int(input("정수: "))
    numberList.append(num)

# 2.계산
for num in numberList:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# 3.출력
print(f"짝수의 합 : {even_sum}")
print(f"홀수의 합 : {odd_sum}")