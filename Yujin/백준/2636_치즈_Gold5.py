import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def meltCheeze():
    q = deque()
    q.append([0, 0])
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True
    cnt = 0

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if cheeze[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append([nr, nc])
                elif cheeze[nr][nc] == 1:
                    cnt += 1
                    cheeze[nr][nc] = 0
                    visited[nr][nc] = True
    total.append(cnt)
    return cnt

N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]

time = 0
total = []
while True:
    time += 1
    cnt = meltCheeze()
    if cnt == 0:
        break

print(time-1)
print(total[-2])



