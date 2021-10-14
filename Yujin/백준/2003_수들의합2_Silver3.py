import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
total = 0
cnt = 0

for start in range(N):
    while total < M and end < N:
        total += arr[end]
        end += 1
    
    if total == M:
        cnt += 1
    total -= arr[start]
    
print(cnt)
