# 실버2 부분수열의 합 : https://www.acmicpc.net/problem/1182
totalCnt = 0


def generateSubSet(cnt, N, M):
    global totalCnt
    if cnt == N:
        sum_out = 0
        for i in range(N):
            if visited[i]:
                sum_out += a[i]

        if sum_out == M:
            totalCnt += 1
            # print(totalCnt)

        return totalCnt

    visited[cnt] = True
    generateSubSet(cnt+1, N, M)

    visited[cnt] = False
    generateSubSet(cnt+1, N, M)


N, M = map(int, input().split())  # N: 숫자갯수, M: 부분수열의 합
a = list(map(int, input().split()))

visited = [False] * N
out = []

generateSubSet(0, N, M)

if M==0:
    print(totalCnt-1)  # 합이 0일때는 공집합이 포함되어 1개 빼줘야함
else:
    print(totalCnt)