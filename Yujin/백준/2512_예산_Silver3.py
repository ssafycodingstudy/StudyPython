import sys
            
N = int(input())
req = list(map(int, input().split()))
M = int(input())

low = 0
high = max(req)

while low <= high:
    mid = (low + high) // 2
    total = 0
    for i in req:
        total += min(i, mid)
    if total > M:
        high = mid - 1
    else:
        low = mid + 1

print(high)