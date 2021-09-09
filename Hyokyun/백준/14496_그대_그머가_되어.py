from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
answer = int(1e9)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False] * (n + 1)


def bfs(start):
    global answer
    q = deque([])
    q.append((start, 0))
    visited[start] = True
    while q:
        now, count = q.popleft()
        if now == b:
            answer = min(answer, count)
            continue
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append((i, count + 1))
    return


bfs(a)
if answer == int(1e9):
    print(-1)
else:
    print(answer)
