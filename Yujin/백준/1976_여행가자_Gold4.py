import sys
input = sys.stdin.readline

def find(a):
	if a == parent[a]: return a
	parent[a] = find(parent[a])
	return parent[a]

def union(a, b):
	A = find(a)
	B = find(b)
	if A < B:
		parent[B] = A
	else:
		parent[A] = B

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

for c in range(N):
	city = list(map(int, input().split()))

	for i in range(len(city)):
		if city[i] == 1:
			union(c+1, i+1)

plan = list(map(int, input().split()))

flag = True
for i in range(M-1):
	if find(plan[i]) != find(plan[i+1]):
		flag = False
		break;

if flag:
	print("YES")
else:
	print("NO")
