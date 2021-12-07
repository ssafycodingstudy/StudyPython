import sys
from itertools import permutations
input = sys.stdin.readline

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
nums = list(permutations(num, 3))

N = int(input())
for _ in range(N):
    n, s, b = map(int, input().split())
    n = list(str(n))
    removeCnt = 0

    for i in range(len(nums)):
        strike, ball = 0, 0
        i -= removeCnt
        for j in range(3):
            if nums[i][j] == n[j]:
                strike += 1
            elif n[j] in nums[i]:
                ball += 1

        if strike != s or ball != b:
            nums.remove(nums[i])
            removeCnt += 1

print(len(nums))
