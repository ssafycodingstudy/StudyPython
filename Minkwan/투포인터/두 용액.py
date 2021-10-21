import sys
max_size = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

i = 0
j = len(arr) -1
pair = []
min_val = max_size

while i < j:
    temp = arr[i] + arr[j]  # 두 값의 합

    # 합의 절대값이 현재 최소값보다 작음
    if abs(temp) < min_val:
        pair = [arr[i], arr[j]]
        min_val = abs(temp)

    # temp값이 0보다 클때 작을떄로 포인터 이동
    if temp >= 0:
        j -= 1
    else:
        i += 1

print(*pair)