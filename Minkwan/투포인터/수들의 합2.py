import sys
n, m = map(int, sys.stdin.readline().split())  # n: 숫자개수, m: 부분합
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, 1  # 시작, 끝 포인터
cnt = 0

while right <= n and left <= right:
    sub = arr[left:right]  # 부분배열 잘라버려
    total = sum(sub)

    if total == m:
        cnt += 1
        right += 1
    elif total < m:  # 합이 부분합보다 작으면 끝포인터 +1하고 추가로 더해주기
        right += 1
    else:  # 합이 부분합보다 작으면 시작포인터를 늘려서 더 적게 더해보기
        left += 1

print(cnt)







