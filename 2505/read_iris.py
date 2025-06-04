f = open("../iris.csv", 'r')
line = f.readline()   # 첫 줄은 타이틀
titles = line.strip().split(',')

irisList = []
line = f.readline() # 타이틀 다음 거 받아놓기 (iris 값)

while line != "":
    splitList = line.strip().split(',')

    dic = {}
    dic["sepal_length"] = float(splitList[0])
    dic["sepal_width"] = float(splitList[1])
    dic["petal_length"] = float(splitList[2])
    dic["petal_width"] = float(splitList[3])
    dic["species"] = splitList[4]
    irisList.append(dic)

    line = f.readline()
f.close()


sl_avg = 0
sw_avg = 0
pl_avg = 0
pw_avg = 0

irisDic = {}

#print(f"{titles[0]}\t{titles[1]}\t{titles[2]}\t{titles[3]}\t{titles[4]}")
for s in irisList:
    #print(f"{s["sepal_length"]}\t{s["sepal_width"]}\t{s["petal_length"]}\t{s["petal_width"]}\t{s["species"]}")
    sl_avg += s["sepal_length"]
    sw_avg += s["sepal_width"]
    pl_avg += s["petal_length"]
    pw_avg += s["petal_width"]

    species = s["species"]
    if species not in irisDic.keys():
        irisDic[species] = 1
    else:
        irisDic[species] += 1

sl_avg /= len(irisList)
sw_avg /= len(irisList)
pl_avg /= len(irisList)
pw_avg /= len(irisList)

print("sl_avg\tsw_avg\tpl_avg\tpw_avg")
print(f"{sl_avg:.2f}\t{sw_avg:.2f}\t{pl_avg:.2f}\t{pw_avg:.2f}")

print()
for key in irisDic.keys():
    print(f"{key}: {irisDic[key]}")