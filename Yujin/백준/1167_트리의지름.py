# 백준 골드3 트리의 지름
import sys
input = sys.stdin.readline

v = int(input()) # 정점 개수

tree = [[] for _ in range(v+1)]

# 트리 입력
for _ in range(v): 
    path = list(map(int, input().split()))

    for i in range(1, len(path)//2):
        tree[path[0]].append([path[i*2-1], path[i*2]]) 

first = [0 for _ in range(v+1)]

def dfs(start, tree, first):
    for e, d in tree[start]:
        if first[e] == 0:
            first[e] = first[start] + d
            dfs(e, tree, first)

dfs(1, tree, first) # 첫번째 dfs -> 임의의 x 에서 가장 먼 y를 찾는다
first[1] = 0 # 1에서 1은 0

max_dist = 0
index = 0

for i in range(len(first)):
    if max_dist < first[i]:
        max_dist = first[i]
        index = i

second = [0 for _ in range(v+1)]

dfs(index, tree, second) # 두번째 dfs -> y에서 가장 먼 z 를 찾는다
second[index] = 0

print(max(second))

