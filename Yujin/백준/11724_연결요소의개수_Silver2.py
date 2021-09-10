import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1   

def bfs(index):
    visited[index] = True
    q = [index]
    while q:
        cur = q.pop(0)
        for i in range(1, N+1):
            if arr[cur][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)
