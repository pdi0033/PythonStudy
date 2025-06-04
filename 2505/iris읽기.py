f = open("../iris.csv", 'r')
lines = f.readlines()   # 첫 줄은 타이틀

irisList = []

for i in range(1, len(lines)):
    line = lines[i]
    line = line[:len(line)-1]
    #print(line)
    values = line.split(',')
    data = [float(values[0]), float(values[1]), float(values[2]), float(values[3]), (values[4])]
    irisList.append(data)
f.close()

# for iris in irisList:
#     print(iris)

result = [0,0,0,0]
for j in range(0,4):
    for i in range(0, len(irisList)):
        result[j] += irisList[i][j]

#print(result[0]/150, result[1]/150, result[2]/150, result[3]/150)

count = len(irisList)
for i in range(0,4):
    print(f"{result[i]/count:.2f}", end='\t')
print()