# while문은 조건에 의해서 특정 조건을 만족할 때만 수행을 한다.
# 때로는 단 한 번도 수행이 안 될 가능성이 있을 때 사용하면 좋다.
# for문 대신에 쓸 수 있다.

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1   # while문이 마지막 문장은 조건이 False가 되는 상황을 만들게 하는 것이 좋다.

"""
num = input("숫자로 입력하세요: ")
while ord(num) < ord('0') or ord(num) > ord('9'):
    print("숫자만 입력하세요 0 ~ 9")
    num = input("숫자로 입력하세요: ")

print("숫자를 입력하셨습니다.")
"""

# 1+2+3+4+... 언제 1000을 넘을까 1000을 넘는 n을 구하려고 할 때

sum = 0
i = 0
while sum < 1000:
    i += 1
    sum += i

print(f"sum: {sum}, i: {i}")