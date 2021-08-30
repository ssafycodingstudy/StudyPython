# 1021번 회전하는 큐 : https://www.acmicpc.net/problem/1021

# 접근 1 : 그냥 배열로 받아서 시도해봤으나 빼내고 다시 미는 과정에서 순탄치 않음... 그냥 deque 이용하기
# 접근 2 : deque 이용해서 문제의 1,2,3번 기능 실제로 이용

from collections import deque

n, m = map(int, input().split())  # n = 큐의크기, m = 뽑아 내려고 하는 수의 개수
a = list(map(int, input().split()))  # 뽑고싶은 숫자를 담은 배열
q = deque([i for i in range(1, n+1)])
count = 0

# print(q)
for num in a:
    while True:
        if q[0] == num:  # 뽑으려는 수가 2,3번 과정거쳐서 0번 인덱스에 오면 내보내버리기
            q.popleft()
            break
        else:
            if q.index(num) <= len(q) // 2:  # 왼쪽으로 밀기
                q.rotate(-1)
                count += 1
            else:  # 오른쪽으로 밀기
                q.rotate(1)
                count += 1

print(count)
