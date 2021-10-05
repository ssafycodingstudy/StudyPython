n = int(input())
request = list(map(int, input().split()))
m = int(input())
answer = 0


def binary_search(target, start, end):
    global answer
    while start <= end:
        total = 0
        # mid는 상한액.
        mid = (start + end) // 2
        for x in request:
            if x < mid:
                total += x
            else:
                total += mid
        # total 값이 예산보다 크다면 상한액을 낮춰야한다.
        if total > target:
            end = mid - 1
        # total 값이 예산보다 작다면 상한액을 키워야한다.
        else:
            answer = mid
            start = mid + 1


if sum(request) <= m:
    print(max(request))
else:
    binary_search(m, 0, max(request))
    print(answer)
