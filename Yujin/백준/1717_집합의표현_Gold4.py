import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    A = find(a)
    B = find(b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B

for _ in range(M):
    order, a, b = map(int, input().split())
    if order == 1:
        if find(a) != find(b):
            print('NO')
        else:
            print('YES')
    else:
        union(a, b)
