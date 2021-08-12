from collections import deque

n = int(input())
k = int(input())
graph = [[0] * n for i in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
l = int(input())
direction = []
for i in range(l):
    a, b = input().split()
    direction.append((int(a), b))

timer = 0

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move(x, y, direction):
    snake = deque([])
    snake.append((x, y))
    q = deque(direction)
    global timer
    # graph[x][y] = 2
    dir = 0  # 오른쪽
    while True:
        for i in range(len(snake)):
            graph[snake[i][0]][snake[i][1]] = 2
        if len(q) != 0:
            if q[0][0] == timer:
                if q[0][1] == 'L': # 왼쪽으로 90도 회전
                    if dir == 0:
                        dir = 3
                    else:
                        dir -= 1
                else: # 오른쪽으로 90도 회전
                    if dir == 3:
                        dir = 0
                    else:
                        dir += 1
                q.popleft()
        timer += 1
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 2:
            return timer
        if graph[nx][ny] == 0:
            ox, oy = snake.popleft()
            graph[ox][oy] = 0
        snake.append((nx, ny))
        x = nx
        y = ny


print(move(0, 0, direction))
