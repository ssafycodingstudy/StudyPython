import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    a, b = map(int, input().split())
    union_parent(a, b, parent)

for i in range(1, n + 1):
    find_parent(parent, i)

dic = set(parent[1:])
print(len(dic))
