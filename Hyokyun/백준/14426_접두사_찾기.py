import sys
n, m = map(int, input().split())
input = sys.stdin.readline
s = [input().strip() for _ in range(n)]
x = [input().strip() for _ in range(m)]
count = 0
for i in x:
    for j in s:
        if i == j[:len(i)]:
            count += 1
            break
print(count)
