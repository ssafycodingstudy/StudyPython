import sys
input = sys.stdin.readline

def find(a):
    if a == parent[a]: return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    A = find(a)
    B = find(b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B

N, M = map(int, input().split())
graph = []

for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()

parent = [i for i in range(N+1)]
road = []

result = 0
for c, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        result += c
        road.append(c)

print(result - road.pop())

