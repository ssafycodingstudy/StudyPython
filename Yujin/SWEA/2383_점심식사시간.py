from itertools import combinations
import heapq

def downStair(team, stair):
    down = []
    time, w_cnt = 0, 0

    while team or down or w_cnt:
        while w_cnt:
            if len(down) == 3:
                break
            down.append(stair[2])
            w_cnt -= 1

        for i in range(len(down)-1, -1, -1):
            down[i] -= 1
            if down[i] <= 0:
                down.pop(i)

        for i in range(len(team)-1, -1, -1):
            team[i] -= 1
            if team[i] <= 0:
                team.pop(i)
                w_cnt += 1
        time += 1
    return time

def dfs(idx):
    if idx == num:
        global last
        stair_1, stair_2 = [], []
        for i in range(num):
            if check[i]: stair_1.append(people[i][0])
            else: stair_2.append(people[i][1])
        cnt = max(downStair(sorted(stair_1), stairs[0]), downStair(sorted(stair_2), stairs[1]))
        last = min(last, cnt)
        return

    check[idx] = True
    dfs(idx+1)
    check[idx] = False
    dfs(idx+1)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    people, stairs = [], []
    num, last = 0, 987654321

    for i in range(N):
        for j in range(N):
            tmp = room[i][j]
            if tmp:
                if room[i][j] == 1:
                    people.append([i, j])
                    num += 1
                else:
                    stairs.append([i, j, room[i][j]])

    for i in range(num):
        dist1 = abs(stairs[0][0] - people[i][0]) + abs(stairs[0][1] - people[i][1])
        dist2 = abs(stairs[1][0] - people[i][0]) + abs(stairs[1][1] - people[i][1])
        people[i][0] = dist1
        people[i][1] = dist2

    check = [False]*num

    dfs(0)
    print("#%d %d" %(tc, last+1))

