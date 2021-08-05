# 더 맵게 - 프로그래머스
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        food = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, food)
        answer += 1
    
    if scoville[0] < K:
        return -1
    else:
        return answer