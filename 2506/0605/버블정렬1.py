import random

def bubbleSort1(arr):
    for i in range(0 ,len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"{i}번째 정렬: {arr}")
    
    return arr

def bubbleSort2(arr):
    for i in range(0 ,len(arr)):
        flag = False    # if문 안에 들어갔었는지 확인하기
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                flag = True     # 데이터 변동이 있었음
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not flag:
            break
        print(f"{i}번째 정렬: {arr}")
    
    return arr

def getArr():
    arr = []
    while True:
        n = random.randint(0, 30)
        if n in arr:
            continue
        arr.append(n)
        if len(arr) >= 10:
            break
    return arr

# arr = [9, 7, 25, 6, 8, 4, 3]
arr = getArr()
print(arr) 
print("-" * 30)
print(bubbleSort1(arr))


print("-" * 30)
arr = getArr()
print(arr) 
print("-" * 30)
print(bubbleSort2(arr))
