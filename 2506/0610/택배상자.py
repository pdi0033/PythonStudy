def solution(n, w, num):
    length = n // w+1   # 행의 개수
    # 2차원 배열: 배열 구조가 아님 [ [], [], [] ],   list of list 구조임
    boxList = []
    for i in range(0, length):
        boxList.append( [None] * w)
    answer = 0

    #  1  2  3 4 5 6  홀수행
    # 12 11 10 9 8 7 짝수행

    k=1     # 계속 증가하면서 값을 저장하기 위해 1~n까지 추적한다.
    for i in range(0, length):
        if i%2 == 0:
            for j in range(0, w):
                if k <= n:
                    boxList[i][j] = k
                    k += 1
        else:
            m = k+w -1      # 시작 위치를 키워놓고
            for j in range(0, w):
                if m <= n:
                    boxList[i][j] = m
                    m -= 1
                    k += 1

    # for i in range(0, length):
    #     print(boxList[i])

    # 해당데이터를 2차원 배열에서 찾아서 행과 열을 가져온다.
    for i in range(0, length):
        if num in boxList[i]:
            row = i
            column = boxList[i].index(num)

    print(row, column)
    answer = length - row   # 전체 행에서 내 위치값 빼기

    cnt = 0
    for i in range(length-1, row-1, -1):
        if boxList[i][column] == None:
            cnt += 1
    
    answer = answer - cnt
    return answer


# 내가 푼 거
import math
def solution1(n, w, num):
    answer = 0
    row = math.ceil(n/w)
    result_arr = []
    for i in range(0, row):
        arr = []
        for j in range(0, w):
            arr.append(0)
        result_arr.append(arr)
    
    for i in range(0, n):
        if (i//w) % 2 == 0:
            result_arr[i//w][i%w] = i+1
        else:
            result_arr[i//w][w-(i%w)-1] = i+1
    
    row = 0
    col = 0
    for i, arr in enumerate(result_arr):
        isFind = False
        for j, value in enumerate(arr):
            if value == num:
                row = i
                col = j
                isFind = True
                break
        if isFind == True:
            break
    print(row)
    answer = len(result_arr)-1 - row
    print(answer)

    if result_arr[len(result_arr)-1][col] != 0:
        answer += 1
            
    print(result_arr)
    print(answer)
    
    return answer

print(solution(22, 6, 8))
print()
print(solution(13, 3, 6))