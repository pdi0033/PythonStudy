def find_prime(num):
    numList = [x for x in range(2, num+1)]

    length = len(numList)
    idx = 0
    while idx < length:
        value = numList[idx]
        idx += 1
        if value == 0:
            continue
        for i in range(idx, len(numList)):
            if numList[i] % value == 0:
                numList[i] = 0

    for n in numList:
        if n != 0:
            print(n, end=' ') 


find_prime(100)

