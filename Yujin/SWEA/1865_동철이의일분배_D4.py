def find(idx, result = 100):
    global maxJ

    if result <= maxJ: return
    if idx >= N:
        maxJ = result
        return
    for i in range(N):
        if check[i]:
            check[i] = False
            find(idx+1, result * jobs[idx][i])
            check[i] = True

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    jobs = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    check = [True]*N
    maxJ = 0
    find(0)

    maxJ = round(maxJ, 6)
    print("#%d %f" %(tc, maxJ))