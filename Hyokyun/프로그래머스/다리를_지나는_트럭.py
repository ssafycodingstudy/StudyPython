from collections import deque

def solution(bridge_length, weight, truck_weights):
    timer = 0
    waiting_truck = deque(truck_weights)
    on_bridge_truck = deque([0] * bridge_length)
    finished_truck = []
    while len(finished_truck) < len(truck_weights):
        if on_bridge_truck[0] != 0:
            finished_truck.append(on_bridge_truck.popleft())
            on_bridge_truck.appendleft(0)
        if len(waiting_truck) != 0 and sum(on_bridge_truck) + waiting_truck[0] <= weight:
            if sum(on_bridge_truck) != 0:
                on_bridge_truck.popleft()
                on_bridge_truck.append(0)
            truck = waiting_truck.popleft()
            on_bridge_truck[-1] = truck
        else:
            if sum(on_bridge_truck) != 0:
                on_bridge_truck.popleft()
                on_bridge_truck.append(0)
        timer += 1
    return timer

# 테스트케이스 5를 시간초과로 통과하지 못한 코드입니다.