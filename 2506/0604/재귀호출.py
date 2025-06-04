# 반드시 언젠가는 끝내야 한다.
# 매개변수를 갖고 다니면서 이 값을 증가 또는 감소를 시켜서 끝나는 상황을 만들어줘야 한다.
# 1~10까지 출력을 하려고 한다.
# 1, 2, 3, ...
def recursive_call(n):
    if n > 10:      # 함수의 종료조건이 중요하다.
        return
    print(n)
    recursive_call(n+1)

def recursive_call2(n):
    if n == 0:
        return
    print(n)
    recursive_call2(n-1)

recursive_call(1)
recursive_call2(10)

# 피보나치 수열
# f(1) = 1
# f(2) = 1
# f(3) = f(1) + f(2) = 2
# f(4) = f(2) + f(3) = 3
# f(5) = f(3) + f(4) = 5
# f(n) = f(n-2) + f(n-1)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

print()
print("3번째요소 ", fibonacci(3))
print("6번째요소 ", fibonacci(6))

# 1~n까지의 합계를 구하는 걸 재귀호출로 작성하기
def recursive_sum(n):
    if n <= 1:
        return 1
    return recursive_sum(n-1) + n

print(f"1~5까지의 합계: {recursive_sum(5)}")
print(f"1~10까지의 합계: {recursive_sum(10)}")

