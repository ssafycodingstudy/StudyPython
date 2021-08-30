# 큐/스택Lv2 다리를 지나는 트럭 : https://programmers.co.kr/learn/courses/30/lessons/42583
""" 1. 지나간 트럭을 넣을 배열, 지나가고있는 트럭 넣을 배열 생성
    2. weight과 truck_weigh를 고려해 지나가고있는 트럭 배열에 한대씩 넣기
    3. lenghth만큼 시간이 지나면 지나고있는 트럭에서 pop으로 빼낸뒤 지나간 트럭에 넣기
    4. 지나간 트럭배열과 truck_weights가 같아지면 그때의 시간을 answer에 넣기
    큐라고 생각하고 맨앞의 값을 계속 받고 내보낸다? -> pop 이용

    접근 1: 콜렉션함수 deque 이용해서 해보려햇지만 실패.......
    접근 2: 끙끙대다 유진님 코드 보면서 이해만 했습니다.. so hard;;;
    """

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리 길이만큼을 배열길이로 넣어줌
    q = [0 for _ in range(bridge_length)]

    while q:  # q가 빌때까지 시간을 더해주기
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


bridge_length1 = 2
weight1 = 10
truck_weight1 = [7, 4, 5, 6]
solution(bridge_length1, weight1, truck_weight1)
answer1 = solution(bridge_length1, weight1, truck_weight1)
print(answer1)  # 8

bridge_length2 = 100
weight2 = 100
truck_weight2 = [10]
answer2 = solution(bridge_length2, weight2, truck_weight2)
print(answer2)  # 101

bridge_length3 = 100
weight3 = 100
truck_weight3 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
answer3 = solution(bridge_length3, weight3, truck_weight3)
print(answer3)  # 110
