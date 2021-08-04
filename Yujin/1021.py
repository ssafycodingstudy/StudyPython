# 회전하는 큐 - 백준

N, M = map(int, input().split())
target = list(map(int, input().split()))
q = [i for i in range(1, N+1)]
cnt = 0

for i in range(M):
    length = len(q)
    index = q.index(target[i])
    if index < length - index: #찾는 인덱스가 중간보다 가깝다면
        while True:
            if q[0] == target[i]: # 처음 위치에 왔을때 pop
                q.pop(0)
                break
            else: # 처음 위치로 갈때까지 계속 이동
                q.append(q[0])
                q.pop(0)
                cnt += 1
    else: # 찾는 인덱스가 중간과 같거나 멀다면
        while True:
            if q[0] == target[i]:
                q.pop(0)
                break
            else:
                q.insert(0, q[-1])
                q.pop()
                cnt += 1
print(cnt)