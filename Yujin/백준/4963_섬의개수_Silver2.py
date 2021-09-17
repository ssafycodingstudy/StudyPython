import sys
input = sys.stdin.readline

dr = [-1, -1, -1, 1, 1, 1, 0, 0]
dc = [-1, 1, 0, -1, 1, 0, -1, 1]

def bfs(r, c):
    q = [[r, c]]
    Map[r][c] = 0
    while q:
        r, c = q.pop(0)
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < h and 0 <= nc < w and Map[nr][nc] == 1:
                q.append([nr, nc])
                Map[nr][nc] = 0

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    Map = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
