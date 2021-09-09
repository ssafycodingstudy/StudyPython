from collections import deque
n, d = map(int, input().split())
graph = [[] for _ in range(10001)]
for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
for i in range(d):
    graph[i].sort(key=lambda x: x[0])
for i in range(d):
    graph[i].append((1, i + 1))
answer = int(1e9)
visited = [False] * 10001


def bfs(start):
    global answer
    q = deque([])
    q.append((start, 0))
    while q:
        now, dist = q.popleft()
        if now == d:
            answer = min(dist, answer)
            continue
        for i in graph[now]:
            if i[1] <= d:
                q.append((i[1], dist + i[0]))


bfs(0)
print(answer)


# 2 10000
# 0 10000 9999
# 1 9999 1
