from collections import deque

w, h = map(int, input().split())


def bfs(x, y):
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    q = deque([])
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > (h - 1) or ny > (w - 1):
                continue
            if graph[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


while w != 0 and h != 0:
    count = 0
    graph = []
    for i in range(h):
        graph.append(list(input().split()))
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '1' and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)
    w, h = map(int, input().split())
