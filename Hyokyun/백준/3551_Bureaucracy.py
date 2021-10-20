import sys
from copy import deepcopy
n = int(input())
arr = [1] * n
input = sys.stdin.readline
laws = []
for _ in range(n):
    s = list(input().split())
    laws.append(s)

temp = deepcopy(laws)
temp.reverse()
idx = n - 1
for law in temp:
    if law[0] == 'cancel' and arr[idx] == 1:
        if arr[int(law[1]) - 1] == 1:
            arr[int(law[1]) - 1] = 0
    idx -= 1

ans = []
for i in range(n):
    if arr[i] == 1:
        ans.append(i + 1)
print(len(ans))
for i in ans:
    print(i, end=' ')
