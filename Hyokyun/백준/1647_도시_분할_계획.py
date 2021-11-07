import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))
graph.sort()


def find_parent(x):
    if parent[x] != x:
        x = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = 0
last = 0
for i in range(m):
    x = graph[i][1]
    y = graph[i][2]
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        result += graph[i][0]
        last = graph[i][0]
    else:
        continue

result -= last
print(result)
