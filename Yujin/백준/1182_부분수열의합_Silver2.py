from itertools import combinations

N, S = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = 0

for i in range(1, N+1):
    for c in combinations(nums, i):
        if sum(c) == S:
            result += 1

print(result)