from itertools import permutations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for str in permutations(nums, M):
    for i in str:
        print(i, end=" ")
    print()