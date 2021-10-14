N = int(input())  # 지방의 수
money = list(map(int, input().split()))  # 지방의 예산 요청
max_m = int(input())  # 총 예산

total_m = sum(money)  # 지방 예산 요청의 총합

money.sort()
start = money[0]  # 지방 예산 요청의 최솟값
end = money[-1]  # 지방 예산 요청의 최댓값

result = 0
if total_m <= max_m:  # 지방 예산 요청의 합이 총 예산보다 작으면 그냥 그대로 주면됨
    print(money[-1])  # 배정된 예산들 중 최댓값은 정렬했을때 맨 뒤의 값
else:  # 그게 아니라면
    while start <= end:  # 이분 탐색 시작
        total = 0
        mid = (start + end) // 2  # 중간값
        for i in range(N):
            if money[i] < mid:
                total += money[i]
            else:
                total += mid
        if total > max_m:
            end = mid - 1
        else:
            result = mid  # 일단은 result에 총예산보다 작게 하는 mid값 저장해놓고 start값 늘려가며 그거보다 더 크게 만족하는 값 있는지 확인
            start = mid + 1
    if result == 0:  # 이분 탐색 했는데 만족하는 값 없는 경우 -> 총예산이 엄청 작은경우 -> 그냥 다 평균돈만큼 줘버리기
        result = max_m // N
    print(result)
