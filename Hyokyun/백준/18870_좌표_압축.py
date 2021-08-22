from copy import deepcopy
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
temp = deepcopy(arr)
temp.sort()
resize = [0] * n
for i in range(1, n):
    if temp[i - 1] < temp[i]:
        resize[i] = resize[i - 1] + 1
    else:
        resize[i] = resize[i - 1]
dict = {}
for i in range(n):
    dict[temp[i]] = resize[i]
for i in range(n):
    print(dict[arr[i]], end=' ')
