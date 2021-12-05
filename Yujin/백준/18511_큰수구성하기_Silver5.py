import sys
from itertools import product
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(str, input().split()))
lenN = len(str(N))
result = 0

maxN = 0
while 1:
    pro = product(numbers, repeat=lenN)

    for num in pro:
        n = int(''.join(num))
        if n <= N:
            result = max(result, n)

    if lenN <= 1:
        print(result)
        break
    else:
        lenN -= 1
