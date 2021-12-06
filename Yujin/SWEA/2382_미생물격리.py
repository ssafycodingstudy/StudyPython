T = int(input())

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    bugs = [list(map(int, input().split())) for _ in range(K)]

    for t in range(M):
        cnt = -1

        visited = [[0]*N for _ in range(N)]

        for bug in bugs:
            cnt += 1
            if bug[2] > 0:
                nr = bug[0] + dr[bug[3]]
                nc = bug[1] + dc[bug[3]]

                if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                    bug[2] = bug[2] // 2

                    if bug[3] == 1 or bug[3] == 3:
                        bug[3] += 1
                    else:
                        bug[3] -= 1
                else:
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = [bug[2], bug[2], cnt]
                    else:
                        if visited[nr][nc][1] > bug[2]:
                            visited[nr][nc][0] += bug[2]
                            bugs[visited[nr][nc][2]][2] = visited[nr][nc][0]
                            bug[2] = 0
                        else:
                            visited[nr][nc][0] += bug[2]
                            visited[nr][nc][1] = bug[2]
                            bugs[visited[nr][nc][2]][2] = 0
                            visited[nr][nc][2] = cnt
                            bug[2] = visited[nr][nc][0]
                bug[0] = nr
                bug[1] = nc
    result = 0
    for bug in bugs:
        result += bug[2]
    print("#%d %d" %(tc, result))