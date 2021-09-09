import heapq

N, D = map(int, input().split())
shortcut = [[] for _ in range(N)]

for i in range(N):
    start, end, dist = map(int, input().split())
    shortcut[i] =  [start, end, dist]
shortcut = sorted(shortcut)

start = 0
km = [0]*10001
for i in range(1, D+1):
    km[i] = km[i-1] + 1
    for cur, end, dist in shortcut:
        if i == end:
            tmp = end - cur
            km[i] = km[cur] + dist if km[i] > km[cur] + dist else km[i]
print(km[D])

