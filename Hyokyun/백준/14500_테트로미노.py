import sys
input = sys.stdin.readline

squares = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (0, 2), (0, 3)], #1
    [(0, 0), (1, 0), (0, 1), (1, 1)], #2
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (-1, 0), (-1, 1), (-1, 2)], #3
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (-1, 1), (-2, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)], #4
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (0, 1), (-1, 1), (1, 1)], #5
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (0, 1), (-1, 1)], #6
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)] #7
]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
total_max = 0
for x in range(n): # 세로
    for y in range(m): # 가로
        for i in range(len(squares)):
            temp_max = 0
            for k in range(4):
                nx = x + squares[i][k][0]
                ny = y + squares[i][k][1]
                if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                    temp_max = 0
                    break
                temp_max += graph[nx][ny]
            total_max = max(temp_max, total_max)

print(total_max)
