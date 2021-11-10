import sys
input = sys.stdin.readline

def dfs(x):
	visited[x] = True
	stack = [x]
	street = [x]

	while stack:
		cur = stack.pop()

		for nx in graph[cur]:
			if not visited[nx]:
				visited[nx] = True
				stack.append(nx)
				street.append(nx)
	return street

def correct(res1, res2):
	for i in res1:
		for j in res2:
			if i == j:
				return i

T = int(input())

for _ in range(T):
	N = int(input())
	graph = [[] for _ in range(N+1)]
	for _ in range(N-1):
		a, b = map(int, input().split())
		graph[b].append(a)

	v1, v2 = map(int, input().split())
	visited = [False]*(N+1)
	result1 = dfs(v1)

	visited = [False]*(N+1)
	result2 = dfs(v2)
	
	print(correct(result1, result2))