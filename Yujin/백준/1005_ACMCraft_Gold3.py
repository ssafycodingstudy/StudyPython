from collections import deque
import sys
input = sys.stdin.readline

# 위상정렬
def topology_sort(): 
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            totalCost[i] = cost[i]

    while q:
        cur = q.popleft()
        
        if cur == W:
            return totalCost[cur]

        for i in graph[cur]:
            indegree[i] -= 1
            totalCost[i] = max(totalCost[i], cost[i] + totalCost[cur])
            if indegree[i] == 0:
                q.append(i)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cost = list(map(int, input().split()))
    cost.insert(0, 0)
    graph = [[] for _ in range(N+1)]
    totalCost = [0]*(N+1)
    indegree = [0]*(N+1)

    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    W = int(input())
    print(topology_sort())