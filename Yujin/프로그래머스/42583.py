# 다리를 지나는 트럭 - 프로그래머스

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리 길이만큼을 배열길이로 넣어줌
    q = [0 for _ in range(bridge_length)]

    while q: # q가 빌때까지 시간을 더해주기
        # 시간(answer)이 1 증가할수록 
        answer += 1
        # q배열이 왼쪽으로 이동
        q.pop(0)
        # 트럭이 더이상 없으면 끝
        if not truck_weights:
            continue
        if weight >= sum(q) + truck_weights[0]:
            q.append(truck_weights.pop(0))
        else:
            q.append(0)

    return answer