import sys
input = sys.stdin.readline

def flip(coins):
    global minC
    for bit in range(2**8):
        coin = [row[:] for row in coins]
        cnt = str(bin(bit))[2:].count('1')
        if minC < cnt:
            continue

        for r in range(3):
            if bit & (1<<r):
                for c in range(3):
                    coin[r][c] = 1 if coin[r][c] == 0 else 0

        for c in range(3):
            if bit & (1<<(c+3)):
                for r in range(3):
                    coin[r][c] = 1 if coin[r][c] == 0 else 0

        if bit & (1<<6):
            for r in range(3):
                coin[r][r] = 1 if coin[r][r] == 0 else 0

        if bit & (1<<7):
            for r in range(3):
                coin[r][2-r] = 1 if coin[r][2-r] == 0 else 0

        sumC = sum(list(map(sum, coin)))
        if sumC == 0 or sumC == 9:
            minC = cnt

T = int(input())

for _ in range(T):
    coins = [list(map(str, input().split())) for _ in range(3)]

    for i in range(3):
        for j in range(3):
            if coins[i][j] == 'T':
                coins[i][j] = 1
            else:
                coins[i][j] = 0
    minC = 987654321
    flip(coins)
    print(-1 if minC == 987654321 else minC)
