import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
city = [[] for _ in range(N+1)]
INF = sys.maxsize

for _ in range(M):
    x, y, sc = map(int, input().split())
    city[x].append((sc, y))

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
dist = [INF]*(N+1)
dist[start] = 0

while q:
    score, cur = heapq.heappop(q)

    # 방문 체크
    if dist[cur] < score: continue

    for sc, nx in city[cur]:
        new_score = score + sc
        if new_score < dist[nx]:
            dist[nx] = new_score
            heapq.heappush(q, (new_score, nx))

print(dist[end])

