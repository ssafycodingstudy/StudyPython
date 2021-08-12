# 트리의 부모 찾기 - 백신
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def DFS(idx, p):
    parent[idx] = p
    if len(arr[idx]) == 0:
        return
    for i in arr[idx]: # 자식 노드에 대해서만 반복
        if parent[i] == 0:
            DFS(i, idx)


N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    r, c = map(int, input().split())
    arr[r].append(c) # 간선 표시
    arr[c].append(r) # 간선 표시

parent = [0 for _ in range(N+1)] # 방문 했는지 확인 & 부모 노드 삽입
for i in arr[1]:
    if parent[i] == 0:
        DFS(i, 1)

for i in range(2, N+1):
    print(parent[i])
