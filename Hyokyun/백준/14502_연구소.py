from copy import deepcopy
from collections import deque
n, m = map(int, input().split())
# n : 세로, m : 가로
graph = [list(map(int, input().split())) for i in range(n)]

dx = [0, 0, -1, 1] # 좌우상하
dy = [-1, 1, 0, 0]
count = 0
answer = 0

# 1. 벽 세 개를 세운다.
# 2. temp 를 만든다.
# 3. 바이러스가 퍼진다.
# 4. 안전영역의 갯수를 구한다.
# 1~4의 과정을 벽 세 개를 모든 i와 j에 대해서 세울때까지 반복한다.

def virus(temp):
    q = deque([])
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))


def count_safe_zone(temp):
    safe_zone = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe_zone += 1
    return safe_zone


def wall():
    global count, answer
    if count == 3:
        temp = deepcopy(graph)
        virus(temp)
        answer = max(answer, count_safe_zone(temp))
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                wall()
                count -= 1
                graph[i][j] = 0


wall()
print(answer)
