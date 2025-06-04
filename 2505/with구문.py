# f = open("../mpg.csv", 'r')
# lines = f.readlines()
# print(lines[:3])

# 거듭해서 여는 건 안 된다.

with open("../mpg.csv", 'r') as f:
    lines = f.readlines()
    print(lines[:3])

    # 알아서 파일 객체가 닫힌다.