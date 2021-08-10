import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
visited = [False] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = deque([])
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                parent[i] = now
                q.append(i)


bfs(1)

for i in range(2, n + 1):
    print(parent[i], end=' ')
