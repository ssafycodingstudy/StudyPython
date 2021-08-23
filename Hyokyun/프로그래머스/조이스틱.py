# name = "JEROEN"	#56
# name = "JAN" #23
name = "ABAAAAAABB" #7
#한 방향으로만 가는것보다 돌아가는게 더 나을 수 있음.


def solution(name):
    n = len(name)
    arr = []
    for i in range(n):
        diff = min((ord(name[i]) - ord('A')), ord('Z') + 1 - (ord(name[i])))
        arr.append(diff)
    count_front = arr[0]
    count_rear = arr[0]
    # 앞에서부터 index를 증가시키면서. 마지막에 연속된 A는 카운트하지 않음.
    len_a = 0
    len_a_max = 0
    for i in range(1, n):
        count_front += 1
        if arr[i] != 0:
            count_front += arr[i]
            len_a_max = max(len_a, len_a_max)
            len_a = 0
        if arr[i] == 0:
            len_a += 1
    count_front = min(count_front - len_a, count_front - len_a_max + 1)
    len_a = 0
    len_a_max = 0
    # vs 뒤에서부터 index를 감소시키면서. 마지막에 연속된 A는 카운트하지 않음.
    for i in range(n - 1, 0, -1):
        count_rear += 1
        if arr[i] != 0:
            count_rear += arr[i]
            len_a_max = max(len_a, len_a_max)
            len_a = 0
        if arr[i] == 0:
            len_a += 1
    count_rear = min(count_rear - len_a, count_rear - len_a_max + 1)
    answer = min(count_front, count_rear)
    return answer


print(solution(name))
