import sys
import heapq

v = 100000
INF = int(1e9)
N, K = map(int, input().split())
graph = [[] for i in range(v + 1)]
graph[0].append((1, 1))
graph[1].append((0, 1))
graph[1].append((2, 0))
for i in range(2, v):
    if i <= 50000:
        graph[i].append((i - 1, 1))
        graph[i].append((i + 1, 1))
        graph[i].append((i * 2, 0))
    else:
        graph[i].append((i - 1, 1))
        graph[i].append((i + 1, 1))
graph[v].append((v - 1, 1))
distance = [INF] * (v + 1)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            if distance[i[0]] < dist:
                continue
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(N)
print(distance[K])
