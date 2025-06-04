def print_line():   # 함수를 정의한다. 메서드
    # pass    # 파이썬은 함수가 되었던 아니면 for, if나 등등 코드가 없이 쓸 수 없다. 대신 pass를 쓴다.
    print("=" * 30)

print_line()    # 함수를 호출한다.
print(print_line()) # 함수에서 반환값을 안 주면 None이 온다.

# 1부터 N까지의 합계를 구하는 함수 만들기
def sigma(limit):    # 작은 프로그램 단위 입출력
    # limit: 매개변수. 매개체를 말한다. 함수 외부에서 함수 내부로 값을 전달하기 위한 목적
    s = 0
    for i in range(1,limit+1):
        s += i
    return s

print(sigma(10))
print(sigma(100))
print(sigma(1000))
print(sigma(10000))