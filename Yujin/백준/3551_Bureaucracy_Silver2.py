N = int(input())
indegree = [1]*(N+1)
laws = []

for i in range(N):
    laws.append(input().split())

for i in range(N-1, -1, -1):
    if laws[i][0] == "declare": continue
    if indegree[i+1] == 1:
        indegree[int(laws[i][1])] -= 1

result = []
for i in range(1, N+1):
    if indegree[i] == 1:
        result.append(i)
print(len(result))
print(*result, sep=" ")