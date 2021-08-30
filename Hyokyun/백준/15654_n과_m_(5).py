import sys
from itertools import permutations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []
for i in permutations(arr, m):
    temp = list(i)
    result.append(temp)

result.sort()
for i in range(len(result)):
    for j in result[i]:
        print(j, end=' ')
    print()
