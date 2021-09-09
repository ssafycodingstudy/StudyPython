import sys, heapq

a, b = map(int, input().split())
N, M = map(int, input().split())
MAX_SIZE = sys.maxsize

arr = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

minCost = [MAX_SIZE]*(N+1)
minCost[a] = 0
q = []
heapq.heappush(q, (0, a))

while q:
    cost, cur = heapq.heappop(q)
    if minCost[cur] < cost: continue

    for next in arr[cur]:
        if minCost[next] > cost + 1:
            minCost[next] = cost + 1
            heapq.heappush(q, (cost + 1, next))

if minCost[b] == MAX_SIZE:
    print(-1)
else:
    print(minCost[b])