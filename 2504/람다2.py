a = [1,2,3,4,5,6,7,8,9,10]
key = 5 # 찾아야할 값
find = -1   # 정수 변수

if find == -1:
    print("not found")
else:
    print(f"{find}번째에 있습니다")

def myFilter(aList, key):
    for i in range(0, len(a)):
        if key == a[i]: # 찾았다.
            return i
    return -1   # for문 다 끝나도 못 찾았다.

pos = myFilter(a, 4)
print(pos)

a = ["red", "green", "blue", "cyan", "gray"]
pos = myFilter(a, "cyan")
print(pos)

a = [
    {"name": "A", "age": 12},
    {"name": "B", "age": 11},
    {"name": "C", "age": 13},
    {"name": "D", "age": 14},
    {"name": "E", "age": 15}
]
pos = myFilter(a, {"name": "C", "age": 34})
print(pos)

def myFilter2(funcKey, a):
    for i in range(0, len(a)):
        if funcKey(a[i]): # 찾았다.
            return i
    return -1   # for문 다 끝나도 못 찾았다.

pos = myFilter2( lambda x: x["name"] == "C", a )
print(pos)


def selectSort(dataList):
    #0 ... 1~n
    #1 ... 2~n
    #2 ... 3~n
    #n-1   n

    # aList = dataList    # 얕은 복사. aList와 dataList데이터는 같다
    aList = [x for x in dataList]   # 컴프리핸션을 이용한 깊은 복사
    for i in range(0, len(aList)-1):
        print(aList)
        for j in range(i+1, len(aList)):
            if aList[i] > aList[j]: # 더 작은 것이 앞에 있어야 한다.
                # aList[i], aList[j] = aList[j], aList[i]
                temp = aList[i]
                aList[i] = aList[j]
                aList[j] = temp

    return aList

def selectSort2(dataList, funcKey):
    aList = [x for x in dataList]   # 컴프리핸션을 이용한 깊은 복사
    for i in range(0, len(aList)-1):
        print(aList)
        for j in range(i+1, len(aList)):
            if funcKey(aList[i], aList[j]): # 더 작은 것이 앞에 있어야 한다.
                aList[i], aList[j] = aList[j], aList[i]
    return aList

def selectSort3(dataList, key):
    aList = [x for x in dataList]   # 컴프리핸션을 이용한 깊은 복사
    for i in range(0, len(aList)-1):
        for j in range(i+1, len(aList)):
            if key(aList[i]) > key(aList[j]): # 더 작은 것이 앞에 있어야 한다.
                aList[i], aList[j] = aList[j], aList[i]
    return aList

a = [5,1,2,4,3]
b = selectSort(a)

print()
print(a)
print(b)
print()

b = sorted(a, key= lambda x: x)
print(a)
print(b)

b = selectSort2(a, lambda x, y: x > y)
print()
print(a)
print(b)

b = selectSort3(a, lambda x: x)
print()
print(a)
print(b)