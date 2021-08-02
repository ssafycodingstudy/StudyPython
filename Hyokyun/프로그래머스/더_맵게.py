import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7


def solution(scoville, K):
    q = []
    answer = 0
    for i in scoville:
        heapq.heappush(q, i)
    while q[0] < K:
        lowest1 = heapq.heappop(q)
        lowest2 = heapq.heappop(q)
        newOne = lowest1 + (lowest2 * 2)
        heapq.heappush(q, newOne)
        answer += 1
        if len(q) == 1 and q[0] < K:
            answer = -1
            break
    return answer


print(solution(scoville, K))
