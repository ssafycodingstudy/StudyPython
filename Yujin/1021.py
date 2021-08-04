# 회전하는 큐 - 백준

N, M = map(int, input().split())
target = list(map(int, input().split()))
q = [i for i in range(1, N+1)]
cnt = 0

for i in range(M):
    length = len(q)
    index = q.index(target[i])
    if index < length - index:
        while True:
            if q[0] == target[i]:
                q.pop(0)
                break
            else:
                q.append(q[0])
                q.pop(0)
                cnt += 1
    else:
        while True:
            if q[0] == target[i]:
                q.pop(0)
                break
            else:
                q.insert(0, q[-1])
                q.pop()
                cnt += 1
print(cnt)