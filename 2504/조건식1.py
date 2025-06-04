# 정수를 하나 입력 받아서 양수일 경우에 본래의 값에 *5를 해서 출력해라

# 숫자인지 확인하기
def is_int(s):
    try:
        int(s)  # 또는 int(s)
        return True
    except ValueError:
        return False

n = input("정수: ")
if is_int(n):
    n = int(n)
    if n > 0:
        n *= 5
    print(n)
else:
    print("정수 값을 입력해주세요.")

# 양수이면 양수라고 출력하고 음수나 0이면 양수아님
if is_int(n):
    n = int(n)
    if n > 0:
        print("양수")
    elif n == 0:
        print("0입니다.")
    else:
        print("음수")
else:
    print("정수 값을 입력해주세요.")