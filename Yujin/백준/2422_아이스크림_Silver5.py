import sys
input = sys.stdin.readline

N, M = map(int, input().split())
creams = [[False]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    creams[a-1][b-1] = True
    creams[b-1][a-1] = True

answer = 0
for i in range(N):
    for j in range(i+1, N):
        if not creams[i][j]:
            for k in range(j+1, N):
                if not creams[i][k] and not creams[j][k]:
                    answer += 1
print(answer)