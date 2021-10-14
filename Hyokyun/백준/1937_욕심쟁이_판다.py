import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
            continue
        if graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


for i in range(n):
    for j in range(n):
        answer = max(dfs(i, j), answer)
print(answer)
