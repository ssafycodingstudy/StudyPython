import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
arr.sort()


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for i in x:
    print(binary_search(i, 0, n - 1), end=' ')
