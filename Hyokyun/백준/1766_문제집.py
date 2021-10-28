import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1


def topology_sort():
    q = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(q, i)
    while q:
        now = heapq.heappop(q)
        print(now, end=' ')
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                heapq.heappush(q, i)


topology_sort()
