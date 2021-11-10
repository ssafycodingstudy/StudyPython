import sys
input = sys.stdin.readline

def dfs(x, dest):
	stack = [(x, dest)]
	maxX = 0
	maxD = 0

	while stack:
		cur, dest = stack.pop()
		if maxD < dest:
			maxD = dest
			maxX = cur

		for nx, cost in graph[cur]:
			if not visited[nx]:
				visited[nx] = True
				stack.append((nx, dest + cost))
	return [maxX, maxD]

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
	graph[b].append((a, c))

visited = [False]*(N+1)
visited[1] = True
maxA = dfs(1, 0)

visited = [False]*(N+1)
visited[maxA[0]] = True
maxB = dfs(maxA[0], 0)
print(maxB[1])