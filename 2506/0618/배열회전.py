# n을 입력하면 n번 회전
# 1번 회전을 n번, L, R

def lrotate(arr):
    # 힘드니까 왼쪽으로 돌기
    # arr = [1,2,3,4,5]
    # arr = [2,3,4,5,1]   # 맨앞의 1이 맨 뒤로 이동
    temp = arr[0]
    # arr[0] = arr[1]
    # arr[1] = arr[2]
    # arr[2] = arr[3]
    # arr[3] = arr[4]
    # arr[4] = temp
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = temp

def rrotate(arr):
    temp = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = temp

def main(arr, n, direction):
    if direction == "L":
        for i in range(0, n):
            lrotate(arr)
    elif direction == "R":
        for i in range(0, n):
            rrotate(arr)

arr = [1,2,3,4,5,6,7,8,9,10]
main(arr, 5, "L")
print(arr)
main(arr, 4, "R")
print(arr)