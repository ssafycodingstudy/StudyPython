import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = {input().strip() for _ in range(n)}
x = [input().strip() for _ in range(m)]
count = 0
for i in x:
    if i in s:
        count += 1
print(count)
