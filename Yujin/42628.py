# 이중우선순위큐 - 프로그래머스
import heapq

def solution(operations):
    answer = [0, 0]
    heap = []
    
    for i in range(len(operations)):
        n, m = operations[i].split()
        m = int(m)
        if n == 'I': # 삽입할때
            heapq.heappush(heap, m)
        elif n == 'D': # 삭제할때
            if heap: # heap에 원소가 있는지 없는지
                if m == 1:
                    heap.pop(-1)
                elif m == -1:
                    heap.pop(0)

    if(heap):
        answer[0] = max(heap)
        answer[1] = min(heap)
        
    return answer