# 1, 2, 3 더하기 - 백준

# 중복순열
from itertools import product
n = int(input())
total = 0
for _ in range(n):
    m = int(input())
    cnt = 0
    for i in range(1, m+1):
        for j in product([1, 2, 3], repeat=i):
            total = sum(j)
            if total == m:
                cnt += 1
    print(cnt)

# DP
import sys
input = sys.stdin.readline
n = int(input())
nums = [0, 1, 2, 4]

for i in range(4, 11):
    nums.append(nums[i-1] + nums[i-2] + nums[i-3])
    
for _ in range(n):
    m = int(input())
    print(nums[m])