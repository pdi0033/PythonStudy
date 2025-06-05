import random

def quickSort1(arr, start, end):
    # 재귀호출이 끝나는 시점
    if start >= end:
        return 
    #기준점
    pivot = arr[start]
    left = start + 1
    right = end
    print(f"left: {left}, right: {right}")
    while left <= right:    # left > right면 배분이 종료한 거라서
        # left 증가시키면서 arr[left]가 pivot 보다 큰 값을 만날 때까지
        # left가 end보다 작은 동안
        while left <= end and arr[left] < pivot:
            left += 1
        while right > start and arr[right] > pivot:
            right -= 1
        print(f"left: {left}, right: {right}")

        if left < right:    # 왼쪽 오른쪽이 서로 자리 바꾸어야 하는 것이 있다.
            arr[left], arr[right] = arr[right], arr[left]
        else:   # 같을 경우
            break
    arr[start], arr[right] = arr[right], arr[start]
    print(arr)
    quickSort1(arr, start, right-1)
    quickSort1(arr, right+1, end)


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

#arr = getArr()
arr = [8, 9, 2, 4, 24, 21, 3, 6, 7, 11, 12]
print(arr) 
print("-" * 30)
print(quickSort1(arr, 0, len(arr)-1))