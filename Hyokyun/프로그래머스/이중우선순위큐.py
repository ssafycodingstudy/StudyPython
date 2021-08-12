import heapq
# operations = ["I 16","D 1"]
operations = ["I 7","I 5","I -5","D -1"]


def solution(operations):
    minQ = []
    maxQ = []
    for i in range(len(operations)):
        print(minQ, maxQ)
        a, b = map(str, operations[i].split(" "))
        if a == 'I':
            heapq.heappush(minQ, int(b))
            heapq.heappush(maxQ, -int(b))
        elif a == "D" and b == "-1":
            if len(minQ) == 0:
                continue
            temp = -(heapq.heappop(minQ))
            for j in range(len(maxQ)):
                if temp == maxQ[j]:
                    maxQ.pop(j)
                    break
        elif a == "D" and b == "1":
            if len(maxQ) == 0:
                continue
            temp = -(heapq.heappop(maxQ))
            for k in range(len(minQ)):
                if temp == minQ[k]:
                    minQ.pop(k)
                    break
    if len(maxQ) == 0:
        answer = [0, 0]
    else:
        print(minQ, maxQ)
        answer = [-(heapq.heappop(maxQ)), heapq.heappop(minQ)]
    return answer


# solution(operations)
print(solution(operations))
