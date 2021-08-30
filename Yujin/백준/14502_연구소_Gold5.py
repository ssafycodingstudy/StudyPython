from copy import deepcopy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 바이러스 뿌리기
def bfs():
    global maxV
    total = 0
    virus = []
    tmp = deepcopy(matrix)
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                virus.append([i, j])
    while virus:
        r, c = virus.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr and nr < N and 0 <= nc and nc < M:
                if tmp[nr][nc] == 0:
                    tmp[nr][nc] = 2
                    virus.append([nr, nc])
    for i in tmp:
        for j in i:
            if j == 0:
                total += 1
    maxV = max(maxV, total)

# 벽 세우기
def setWall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                setWall(cnt+1)
                matrix[i][j] = 0


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
maxV = 0 # 안전 영역 크기 최대
setWall(0)
print(maxV)