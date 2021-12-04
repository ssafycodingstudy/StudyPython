import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))


def dfs(i):
    global temp, radius, dot
    visited[i] = True
    for node in graph[i]:
        if not visited[node[0]]:
            temp += node[1]
            dfs(node[0])
            radius = max(radius, temp)
            if radius == temp:
                dot = node[0]
            temp -= node[1]
    return


dot = 0
radius = 0
temp = 0
dfs(1)
radius = 0
temp = 0
visited = [False] * (n + 1)
dfs(dot)
print(radius)
