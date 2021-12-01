import sys
from collections import deque
input = sys.stdin.readline

dr1, dr2 = [1, 1, 0, 0, -1, -1], [1, 1, 0, 0, -1, -1]
dc1, dc2 = [0, 1, -1, 1, 0, 1], [-1, 0, -1, 1, -1, 0]

def check(dr, dc, r, c, i):
    nr = r + dr[i]
    nc = c + dc[i]
    if 0 <= nr <= H+1 and 0 <= nc <= W+1:
        if not visited[nr][nc]:
            if house[nr][nc] == 0:
                visited[nr][nc] = True
                q.append((nr, nc))

W, H = map(int, input().split())
house = [[0]*(W+2) for _ in range(H+2)]
visited = [[False]*(W+2) for _ in range(H+2)]

for i in range(1, H+1):
    tmp = list(map(int, input().split()))
    for j in range(1, W+1):
        house[i][j] = tmp[j-1]

q = deque([(0, 0)])
visited[0][0] = True

while q:
    r, c = q.popleft()
    for i in range(6):
        if r % 2 == 0:
            check(dr2, dc2, r, c, i)
        else:
            check(dr1, dc1, r, c, i)

answer = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        if house[i][j] == 0: continue
        for k in range(6):
            if i % 2 == 0:
                nr = i + dr2[k]
                nc = j + dc2[k]
            else:
                nr = i + dr1[k]
                nc = j + dc1[k]
            if visited[nr][nc]: answer += 1
print(answer)




