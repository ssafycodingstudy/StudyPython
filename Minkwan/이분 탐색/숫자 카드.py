N = int(input())  # 가지고 있는 숫자 카드 개수
number = list(map(int, input().split()))  # 현재 보유중인 숫자 카드
M = int(input())  # 구분해야할 숫자카드의 개수
compare = list(map(int, input().split()))  # 비교해야할 숫자 카드
number.sort()


def binary_search(number, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if number[mid] == target:
            return 1
        elif number[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for i in range(M):
    target = compare[i]
    print(binary_search(number, target, 0, len(number)-1), end=' ')