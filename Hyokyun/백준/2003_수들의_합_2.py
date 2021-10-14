import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))

end = 0
temp_sum = 0
count = 0
for start in range(n):
    while temp_sum < m and end < n:
        temp_sum += array[end]
        end += 1
    if temp_sum == m:
        count += 1
    temp_sum -= array[start]
print(count)
