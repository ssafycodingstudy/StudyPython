from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def bfs(start, end):
    q = deque([])
    visited[start] = True
    q.append((start, 0))
    while q:
        now, dist = q.popleft()
        if now == end:
            print(dist)
            return
        for i in graph[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                q.append((i[0], dist + i[1]))


for _ in range(m):
    visited = [False] * (n + 1)
    a, b = map(int, input().split())
    bfs(a, b)
