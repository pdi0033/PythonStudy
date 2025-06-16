M = 5       # 열의 개수 - 너비
N = 4       # 행의 개수 - 높이
arr = [
    [1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
]

visited = [[0]*M for _ in range(N)]

def printArray(arr):
    print()
    for a in range(0, len(arr)):
        print(arr[a])

printArray(visited)

# 재귀호출 -> 네브 스택을 사용한다.
def dfs(y, x):
    # 방문 표시
    visited[y][x] = 1
    printArray(visited)
    # 탐색이 가능한 좌표배열을 만든다.
    # 상하좌우 대각선
    dx = [0, 0, -1, 1, -1, -1, 1, 1]    # 좌우
    dy = [1, -1, 0, 0, 1, -1, 1, -1]    # 상하

    # 8방향으로 새로운 좌표를 산출한다. 그래서 이동 가능한지 확인한다.
    for i in range(len(dx)):
        ny = y + dy[i]
        nx = x + dx[i]
        # 이 좌표가 벽이면 다른 좌표 확인하기.
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue    # 이 좌표는 버린다.
        # 방문을 안 했거나 해당 좌표가 1일 경우에는 탐색을 계속한다.
        if visited[ny][nx] == 0 and arr[ny][nx] == 1:
            dfs(ny, nx)     # 새 좌표에서 또 다른 탐색을 진행한다.
    print(y, x)

def solution(arr, M, N):
    island_cnt = 0  # 섬의 개수 0
    for i in range(0, N):   # 행, 높이
        for j in range(0, M):   # 열, 너비
            # 방문 안 했고 섬이어야 dfs 호출하기
            if visited[i][j] == 0 and arr[i][j] == 1:
                dfs(i, j)   # 탐색 한번 할 때마다
                island_cnt += 1

    return island_cnt
print(solution(arr, M, N))



