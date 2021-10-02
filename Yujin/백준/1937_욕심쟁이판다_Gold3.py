import sys
sys.setrecursionlimit(3000)
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    global cnt
    if dp[r][c] != 0:
        return dp[r][c]
    dp[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and forest[r][c] < forest[nr][nc]:
            tmp = 1
            tmp += dfs(nr, nc)
            dp[r][c] = max(dp[r][c], tmp)
            if dp[r][c] > cnt:
                cnt = dp[r][c]
    return dp[r][c]
    

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        dfs(i, j)
print(cnt)