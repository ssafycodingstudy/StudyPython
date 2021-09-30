import sys

n = int(sys.stdin.readline())  # 1 <= n <= 1000

arr = []
arr.append(0)
arr.append(1)
arr.append(2)

i = 3
while i <= n:
    arr.append(arr[i-2] + arr[i-1])
    i += 1

print(arr[n]%10007)
