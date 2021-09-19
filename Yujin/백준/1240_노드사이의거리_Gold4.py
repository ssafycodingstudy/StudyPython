import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 987654321
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y, s = map(int, input().split())
    arr[x].append((s, y))
    arr[y].append((s, x))

def dijkstra(a):
    dist = [INF]*(N+1)
    dist[a] = 0
    q = []
    heapq.heappush(q, (dist[a], a))
    while q:
        score, cur = heapq.heappop(q)
        if dist[cur] < score: continue

        if cur == end:
            print(dist[cur])
            return

        for sc, nx in arr[cur]:
            next_score = score + sc
            if next_score < dist[nx]:
                dist[nx] = next_score
                heapq.heappush(q, (next_score, nx))
    

for _ in range(M):
    start, end = map(int, input().split())
    dijkstra(start)