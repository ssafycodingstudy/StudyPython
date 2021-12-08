import sys
input = sys.stdin.readline

def fourSquares(N):
    if (N**0.5).is_integer():
        return 1
    for i in range(1, int(N**0.5)+1):
        if N < i ** 2:
            break
        if ((N - i ** 2) ** 0.5).is_integer():
            return 2
    for i in range(1, int(N**0.5) + 1):
        if N < i ** 2:
            break
        for j in range(1, int((N - i ** 2) ** 0.5) + 1):
            if N < i ** 2 + j ** 2:
                break
            if ((N - i ** 2 - j ** 2) ** 0.5).is_integer():
                return 3
    return 4

N = int(input())
print(fourSquares(N))