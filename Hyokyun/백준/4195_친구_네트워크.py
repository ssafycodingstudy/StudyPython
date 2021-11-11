import sys
sys.setrecursionlimit(int(1e5))

input = sys.stdin.readline
tc = int(input())


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[b] = a
        friends[a] += friends[b]
    print(friends[a])


for _ in range(tc):
    f = int(input())
    parent = {}
    friends = {}
    for _ in range(f):
        a, b = map(str, input().split())
        if a not in parent:
            parent[a] = a
            friends[a] = 1
        if b not in parent:
            parent[b] = b
            friends[b] = 1
        union_parent(a, b)
