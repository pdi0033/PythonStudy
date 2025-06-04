f = open("정수.txt", "r")
intList = f.readlines()

# 뒤의 \n 삭제
for i in intList:
    if '\n' in i:
        i = i[:len(i)-1]
    print(i)

avg = 0
for i in intList:
    avg += int(i)
avg = avg / len(intList)
print(f"평균: {avg:.2f}")
f.close()

#찹다