import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())

arr = [[0] * (N + 1)]
for i in range(N):
    arr.append([0] + list(map(int, input().split())))

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if arr[i][j] == 1:
            union_parent(parent, i, j)

visitCity = list(map(int, input().split()))

check = True
for i in range(M - 1):
    if find_parent(parent, visitCity[i]) != find_parent(parent, visitCity[i + 1]):
        check = False
        break

if check:
    print('YES')
else:
    print('NO')
