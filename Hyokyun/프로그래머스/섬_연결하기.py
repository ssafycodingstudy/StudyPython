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


def solution(n, costs):
    graph = []
    m = len(costs)
    answer = 0
    parent = [0] * n
    for i in range(n):
        parent[i] = i
    for i in range(m):
        graph.append((costs[i][2], costs[i][0], costs[i][1]))
    graph.sort()
    for i in range(m):
        if find_parent(parent, graph[i][1]) != find_parent(parent, graph[i][2]):
            union_parent(parent, graph[i][1], graph[i][2])
            answer += graph[i][0]
        else:
            continue
    return answer