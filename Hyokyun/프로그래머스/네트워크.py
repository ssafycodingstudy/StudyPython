from collections import deque
n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(computers, i, visited)
    return answer


def bfs(computers, start, visited):
    q = deque([])
    visited[start] = False
    q.append(start)
    while q:
        now = q.popleft()
        for i in range(len(computers[now])):
            if computers[now][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)


print(solution(n, computers))
