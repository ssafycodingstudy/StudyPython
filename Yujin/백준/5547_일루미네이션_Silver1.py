import sys
from collections import deque
input = sys.stdin.readline

dr1, dr2 = [1, 1, 0, 0, -1, -1], [0, 1, -1, 1, 0, 1]
dc1, dc2 = [0, 1, -1, 1, 0, 1], [-1, 0, -1, 1, -1, 0]

def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = True
    while q:
        r, c = q.popleft()
        if r == 0 or r % 2 == 0:
            for k in range(6):
                nr = r + dr1[k]
                nc = c + dc1[k]
                if 0 > nr or nr >= H or 0 > nc or nc >= W: continue
                if house[nr][nc] == 1:
                    print(r, c, nr, nc)
                    wall[r][c] += 1
                    if not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
        else:
            for k in range(6):
                nr = r + dr2[k]
                nc = c + dc2[k]
                if 0 > nr or nr >= H or 0 > nc or nc >= W: continue
                if house[nr][nc] == 1:
                    print(r, c, nr, nc)
                    wall[r][c] += 1
                    if not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True

W, H = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(H)]
wall = [[0]*W for _ in range(H)]
visited = [[False]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if house[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
print(*wall, sep="\n")