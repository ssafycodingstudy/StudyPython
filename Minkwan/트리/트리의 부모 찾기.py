# 트리의 부모 찾기 : https://www.acmicpc.net/problem/11725

# 1을 루트로해서 bf를 쓰기 <- 아직 BFS DFS 쓰는법이 익숙하지가 않아서 찾아봐서함..

n = int(input())
tree = [[]for i in range(n+1)]

for i in range(n-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

# print(tree)
# print(a)
# print(b)

q = [1]
ans = {}
check = [False for i in range(n+1)]

while len(q)>0:
    parent = q.pop(0)
    for i in tree[parent]:
        if not check[i]:
            ans[i] = parent
            q.append(i)
            check[i] = True

for  i in range(2, n+1):
    print(ans[i])