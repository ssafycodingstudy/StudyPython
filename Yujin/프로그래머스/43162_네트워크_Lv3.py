n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            answer += 1
            q = [i]
            visited[i] = True
            while q:
                x = q.pop(0)
                for j in range(n):
                    if computers[x][j] == 1 and not visited[j]:
                        q.append(j)
                        visited[j] = True
    return answer

print(solution(n, computers))