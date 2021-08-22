# 뱀  - 백준
from collections import deque
N = int(input())
K = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

# 사과 위치 저장
for _ in range(K): 
    y, x = map(int, input().split())
    arr[y-1][x-1] = 1

# 방향 변환 저장
l = int(input())
time = {}
for _ in range(l):
    sec, dir = input().split()
    sec = int(sec)
    time[sec] = dir

dr = [-1, 0, 1, 0] # 상 우 하 좌
dc = [0, 1, 0, -1]
def move():
    second = 0 # 걸리는 시간
    diff = 1
    q = deque([[0, 0]])
    arr[0][0] = 2
    while True:
        r, c = q.popleft()
        nr = r + dr[diff]
        nc = c + dc[diff]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 2:
            second += 1
            # 방향 전환 시간이 됐을때
            if second in time.keys() and time[second] == 'L':
                diff = (diff + 3) % 4
            elif second in time.keys() and time[second] == 'D':
                diff = (diff + 1) % 4
            
            # 사과 먹을 때
            q.appendleft([r, c])
            if arr[nr][nc] != 1:
                del_y, del_x = q.pop()
                if nr == del_y and nc == del_x: # 머리를 먼저 늘려서 꼬리랑 만나는지 확인
                    return second
                arr[del_y][del_x] = 0 
            q.appendleft([nr, nc])
            arr[nr][nc] = 2
        else:
            return second+1

result = move()
print(result)
