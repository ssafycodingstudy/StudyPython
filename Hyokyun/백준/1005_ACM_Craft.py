import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def topology_sort():
    q = deque([])
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + time[i], dp[i])
            if indegree[i] == 0:
                q.append(i)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    time = [0] + list(map(int, input().split()))
    dp = deepcopy(time)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(input())
    result = []
    topology_sort()
    print(dp[w])


# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
