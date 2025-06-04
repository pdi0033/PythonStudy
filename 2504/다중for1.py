# for문 안에서 또 for문이 작동하는 경우
# for i in range(1,6):
#     for j in range(1,6):
#         print(f"i={i}, j={j}")

# 문제1. 이중 for문 사용해서 1~100까지 출력.
# 한 줄에 10개씩
k = 1
for i in range(0,10) :
    for j in range(1, 11):
        print(f"{i*10 + j}", end = "\t")
        # print(f"{k}, end = "\t")
        # k += 1
    print()

# 문제2. 이중 for문
# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# ...
# 이렇게 10개쯤 (+10 나오면 됨)

for i in range(1,11):
    sum = 0
    for j in range(1, i+1):
        if j != 1:
            print(" + ", end = "")
        sum += j
        print(f"{j}", end = "")
    print(f" = {sum}")

for i in range(1, 11):
    sum = 0 
    for j in range(1, i+1):
        if j<i:
            print(j, end=" + ")
        else:
            print(j, end=" = ")
        sum += j
    print (sum)

for i in range(0, 10):
    for j in range(0, i):
        print("*", end="")
    print()

for i in range(0, 10):
    print("*" * i)


"""
     *          별: 1   공백: 3     라인: 1     별의 개수: 2*라인수 - 1     공백: 4 - 라인
    ***         별: 3   공백: 2     라인: 2
   *****        별: 5   공백: 1     라인: 3
  *******       별: 7   공백: 0     라인: 4
   *****        별: 5   공백: 1     라인: 1     (LINES-공백)*2 + 1
    ***         별: 3   공백: 2     라인: 2
     *          별: 1   공백: 3     라인: 3
"""
print()

for i in range(1, 8):
    if i <= 4:
        print(" " * (8 - i) + "*" * (i*2 - 1))
    else:
        print(" " * (i) + "*" * ((8 - i)*2 - 1))

print()

LINES = 7
for i in range(1, LINES+1):
    if i <= 4:
        print(" " * (LINES-i), end="")
        print("*" * (2*i - 1))

for i in range(1, LINES+1):
    for j in range(0, (LINES-i)):
        print(" ", end="")
    for j in range(0, 2*i -1):
        print("*", end="")
    print()

LINES = LINES-1
for i in range(0, LINES+1):
    for j in range(0, i):
        print(" ", end="")
    for j in range(0, (LINES-i)*2 + 1):
        print("*", end="")
    print()