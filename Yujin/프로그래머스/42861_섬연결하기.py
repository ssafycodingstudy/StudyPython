import heapq
import sys      
# Prim 알고리즘
def solution(n, costs):
    answer = 0
    visited = [False]*n
    matrix = [[]*n for _ in range(n)]
    minCost = []

    for a, b, cost in costs:
        matrix[a].append((cost, b))
        matrix[b].append((cost, a))

    heapq.heappush(minCost, (0, 0))

    while False in visited:
        cost, start = heapq.heappop(minCost)
        if visited[start]: continue

        visited[start] = True
        answer += cost

        for cost, end in matrix[start]:
            if visited[end]: continue
            heapq.heappush(minCost, (cost, end))

    return answer

# Kruskal 알고리즘
def solution(n, costs):
    answer = 0
    visited = [False]*n
    matrix = [[]*n for _ in range(n)]
    minCost = []

    for a, b, cost in range(len(costs)):
        matrix[a][b] = matrix[b][a] = cost

    for i in range(len(costs)):
        r = costs[i][0]
        c = costs[i][1]
        matrix[r][c] = matrix[c][r] = costs[i][2]
        
    for i in range(n):
        minCost[i] = sys.maxsize
    answer = 0
    minCost[0] = 0

    for i in range(n):
        tmp = sys.maxsize
        minIndex = -1
        for j in range(n):
            if not visited[j] and tmp > minCost[j]:
                minIndex = j
                tmp = minCost[j]

        visited[minIndex] = True
        answer += tmp

        for j in range(n):
            if not visited[j] and matrix[minIndex][j] != 0 and minCost[j] > matrix[minIndex][j]:
                minCost[j] = matrix[minIndex][j]
    
    return answer