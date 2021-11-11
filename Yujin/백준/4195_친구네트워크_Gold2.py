import sys
input = sys.stdin.readline

def find(a):
	if a == parents[a]: return a
	parents[a] = find(parents[a])
	return parents[a]

def union(a, b):
	A = find(a)
	B = find(b)
	if A != B:
		parents[B] = A
		fNum[A] += fNum[B]
	print(fNum[A])

F = int(input())

for _ in range(F):
	N = int(input())
	parents = {}
	fNum = {}
	cnt = 0

	for _ in range(N):
		a, b = map(str, input().split())
		if a not in parents:
			parents[a] = a
			fNum[a] = 1
		if b not in parents:
			parents[b] = b
			fNum[b] = 1
		union(a, b)
