import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
t = int(input())


def dfs(x, arr):
    for parent in graph[x]:
        arr.append(parent)
        dfs(parent, arr)


for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[b].append(a)
    last_a, last_b = map(int, input().split())
    parent_a = [last_a]
    parent_b = [last_b]
    dfs(last_a, parent_a)
    dfs(last_b, parent_b)
    check = False
    for x in parent_a:
        for y in parent_b:
            if x == y:
                print(x)
                check = True
                break
        if check:
            break
