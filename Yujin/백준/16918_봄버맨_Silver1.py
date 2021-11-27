import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    pan[r][c] = '.'

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 > nr or nr >= R or 0 > nc or nc >= C or pan[nr][nc] == 'O': continue
        pan[nr][nc] = '.'


R, C, N = map(int, input().split())
pan = [list(input().rstrip()) for _ in range(R)]

if N % 2 == 0:
    for i in range(R):
        for j in range(C):
            print('O', end="")
        print()
else:
    if N == 1:
        for i in range(R):
            for j in range(C):
                print(pan[i][j], end="")
            print()
    else:
        for i in range(R):
            for j in range(C):
                if pan[i][j] == '.':
                    pan[i][j] = 'X'
        for i in range(R):
            for j in range(C):
                if pan[i][j] == 'O':
                    bfs(i, j)
        if (N-3) % 4 == 0:
            for i in range(R):
                for j in range(C):
                    if pan[i][j] == 'X':
                        pan[i][j] = 'O'
            for i in range(R):
                for j in range(C):
                    print(pan[i][j], end="")
                print()
        else:
            for i in range(R):
                for j in range(C):
                    if pan[i][j] == 'X':
                        pan[i][j] = 'O'
                    else:
                        pan[i][j] = 'X'
            for i in range(R):
                for j in range(C):
                    if pan[i][j] == 'O':
                        bfs(i, j)
            for i in range(R):
                for j in range(C):
                    if pan[i][j] == 'X':
                        print('O', end="")
                    else:
                        print(pan[i][j], end="")
                print()
