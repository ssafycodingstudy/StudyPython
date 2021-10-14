import sys
input = sys.stdin.readline

def binarySearch(target):
    low = 0
    high = N - 1
    while low <= high:
        mid = (low + high) // 2
        if sangCard[mid] < target:
            low = mid + 1
        elif sangCard[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

N = int(input())
sangCard = list(map(int, input().split()))
M = int(input())
mCard = list(map(int, input().split()))

sangCard.sort()

low = 0
for i in range(M):
    if binarySearch(mCard[i]) != -1:
        print("1", end=" ")
    else:
        print("0", end=" ")