# 그저 BFS.......
from collections import deque

N, M = map(int, input().split())
visited = [False] * (N + 1)  # 방문했는지 안했는지 확인
graph = [[] for _ in range(N + 1)]  # 그래프

for _ in range(M):
    x, y = map(int, input().split()) # 간선의 양 끝점
graph[x].append(y)
graph[y].append(x)


def bfs(v):
    q = deque()


q.append(v)

while q:
    x = q.popleft()
    if visited[x] == False:
        visited[x] = True
    for i in graph[x]:
        q.append(i)

cnt = 0
for i in range(1, N + 1):
    if visited[i] == False:
        bfs(i)
    cnt += 1

print(cnt)