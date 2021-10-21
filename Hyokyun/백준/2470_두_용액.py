import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
start = 0
end = n - 1
cur_start = 0
cur_end = 0
ans = int(1e10)

while start < end:
    temp = arr[start] + arr[end]
    if abs(temp) <= ans:
        ans = abs(temp)
        cur_start = arr[start]
        cur_end = arr[end]
    if temp == 0:
        break
    elif temp < 0:
        start += 1
    else:
        end -= 1
print(cur_start, cur_end)
