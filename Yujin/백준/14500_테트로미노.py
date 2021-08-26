d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dd = [[(0, -1), (-1, 0), (0, 1)], [(0, -1), (1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(-1, 0), (0, -1), (1, 0)]]

# 산모양 테트로미노일 경우
def notdfs(r, c):
    global result
    for dir in dd:
        total = matrix[r][c]
        for i in range(3):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            if 0 <= nr < N and 0 <= nc < M:
                total += matrix[nr][nc]
            else:
                break
        result = max(result, total)

# 그외 테트로미노일 경우
def dfs(r, c, total, visited):
    global result
    if len(visited) == 4:
        result = max(result, total)
        return
    for i in range(4):
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < N and 0 <= nc < M:
            if (nr, nc) not in visited:
                visited.append((nr, nc))
                dfs(nr, nc, total + matrix[nr][nc], visited)
                visited.pop()

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = 0

# 처음부터 하나씩 시도해봄
for r in range(N):
    for c in range(M):
        dfs(r, c, matrix[r][c], [(r, c)])
        notdfs(r, c)
print(result)
