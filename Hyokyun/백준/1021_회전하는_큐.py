from collections import deque

n, m = map(int, input().split())

arr = [(i + 1) for i in range(n)]
# print(arr)
answer = list(map(int, input().split()))
q = deque(arr)
# print(answer)
count = 0
for find in answer:
    flag = False
    for i in range(len(q)):
        if find == q[i]:
            if i <= len(q) // 2:
                #popleft 수행
                while q:
                    now = q.popleft()
                    if now == find:
                        flag = True
                        break
                    q.append(now)
                    count += 1
                # print("popleft 수행")
            else:
                #popright 수행
                while q:
                    now = q.pop()
                    if now == find:
                        count += 1
                        flag = True
                        break
                    q.appendleft(now)
                    count += 1
                # print("pop 수행")
        if flag:
            # print(count)
            # print(q)
            # print('----------')
            break

print(count)