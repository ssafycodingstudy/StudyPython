import sys
N = int(input())

arr = list(map(int,input().split()))

arr.sort()
start = 0
end = N-1

total = abs(arr[start] + arr[end])
rs = start
re = end

while start < end:
    tmp = arr[start] + arr[end]
    if abs(tmp) < abs(total):
        tmp = total
        rs = start
        re = end
        if tmp == 0:
            break
    if tmp < 0:
        start += 1
    else:
        end -= 1
print(arr[rs], arr[re])