
def getIndex(a):
    b = [x for x in a]
    b.sort()
    b = list(set(b))
    print(b)
    index = []
    for i in a:
        ii = b.index(i)
        index.append(ii)
    return index

a = [12, 50, 31]
a1 = [1,3,2]
a2 = [12,50,31]
print(getIndex(a1), getIndex(a2))


numList = [[20,10,30],
           [10,20,60]]