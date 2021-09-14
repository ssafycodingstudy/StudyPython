import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

dr = [-1, -1, -1, 1, 1, 1, 0, 0]
dc = [-1, 1, 0, -1, 1, 0, -1, 1]

def dfs(r, c):
    Map[r][c] = 0
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < h and 0 <= nc < w and Map[nr][nc] == 1:
            dfs(nr, nc)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    Map = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)

