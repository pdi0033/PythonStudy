# https://wikidocs.net/206317

"""
str -> list -> map(int, ) -> list

6 6
0 1 1 1 1 1
0 1 0 0 0 1
0 1 0 1 0 1
0 1 0 1 0 0 
0 0 0 1 1 0
1 1 1 1 1 0
"""

# map은 list의 요소에 앞에서 전달해준 수식 또는 함수를 적용한다.
# N, M = map(int, input().split())  # 문장으로 받는다. 문장을 잘라줘서 단어로 만든다.
# # print(N, M)
# arr = []
# for i in range(N):
#     # map 함수는 iterable이다. 아직 진행이 안 돼서 list를 써줘야 진행된다.
#     temp = map(int, input().split())
#     arr.append( list(temp) )

N, M = 6, 6
arr = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0], 
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
]

def printArray(arr, N):
    for i in range(0, N):
        print( arr[i] )

printArray(arr, N)

"""
둘러싸고 있는 공간.  상하좌우4  대각선4방향
1,0   0,0   2,0
방문 테이블을 만들어 내가 갔던 위치를 1로 바꿔쳐서 다 표시를 한다.
"""
# 방문테이블
# 파이썬 미리 메모릴 할당 1차원  []*개수
visited = [ [False] * M for _ in range(N) ]
# visited = []
# for i in range(N):
#     visited.append( [False]* M)
printArray(visited, N)

# 깊이우선 탐색
def dfs(y, x):
    # 매개변수로 전달받는 좌표는 현재 위치값
    visited[y][x] = True    # 방문함

    # 현재좌표로부터 4방향 내지는 8방향을 확인해볼 수 있다.
    dx = [-1, 1, 0, 0]  # 좌우
    dy = [0, 0, -1, 1]  # 상하      변이: 이동값
    # dx = [-1, 1, 0, 0, -1, -1, 1, 1]   대각선
    
    for i in range(len(dx)):
        # 새로운 좌표점을 찾는다.
        ny = dy[i] + y
        nx = dx[i] + x
        # 새좌표가 벽일 수도 있고 이미 방문했던 곳일 수도 있다.
        if not (0 <= nx < N and 0 <= ny < M):     # 벽이라면
            continue    # 다시 for문 처음으로 되돌아가라.
        if arr[ny][nx] == 1:
            continue
        if not visited[ny][nx]:     # 아직 방문 안 했으면
            dfs(ny, nx)     # 새로운 출발점으로 해서 재귀호출. 시스템 내부 스택

print()
dfs(0, 0)
printArray(visited, N)