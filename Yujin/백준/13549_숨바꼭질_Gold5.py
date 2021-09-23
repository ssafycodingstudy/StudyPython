# dijkstra
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
N, K = map(int, input().split())

time = [INF]*100001

def dijkstra(N):
    q = []
    heapq.heappush(q, (0, N))
    
    while q:
        second, cur = heapq.heappop(q)

        if time[cur] < second: continue
        if cur == K:
            print(second)
            break

        for i in range(3):
            new_second = second + 1
            if i == 0:
                nx = cur * 2
                new_second -= 1
            elif i == 1:
                nx = cur - 1
            elif i == 2:
                nx = cur + 1
            if 0 <= nx <= 100000 and new_second < time[nx]:
                time[nx] = new_second
                heapq.heappush(q, (new_second, nx))
                
dijkstra(N)

#bfs
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
N, K = map(int, input().split())

time = [-1]*100001
time[N] = 0

def bfs(N):
    q = []
    q.append(N)
    
    while q:
        dist = q.pop(0)
        if dist == K:
            print(time[dist])
            break
        
        if 0 <= dist*2 <= 100000 and time[dist*2] == -1:
            time[dist*2] = time[dist]
            q.append(dist*2)
        if 0 <= dist-1 <= 100000 and time[dist-1] == -1:
            time[dist-1] = time[dist] + 1
            q.append(dist-1)
        if 0 <= dist+1 <= 100000 and time[dist+1] == -1:
            time[dist+1] = time[dist] + 1
            q.append(dist+1)

bfs(N)