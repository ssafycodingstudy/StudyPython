import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) + 1, 2):
        if arr[i] == -1:
            break
        # 정점, 거리
        graph[arr[0]].append((arr[i], arr[i + 1]))
        graph[arr[i]].append((arr[0], arr[i + 1]))


def dfs(x, distance):
    global max_dist, max_node
    visited[x] = True
    for i in graph[x]:
        if not visited[i[0]]:
            visited[i[0]] = True
            distance += i[1]
            max_dist = max(distance, max_dist)
            if max_dist == distance:
                max_node = i[0]
            dfs(i[0], distance)
            distance -= i[1]


max_node = 0
max_dist = 0
temp_dist = 0
dfs(1, temp_dist)
max_dist = 0
temp_dist = 0
visited = [False] * (n + 1)
dfs(max_node, temp_dist)
print(max_dist)
