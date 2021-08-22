# 좌표압축 - 백준
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
num = sorted(set(arr)) # 중복 없애기

res = {num[i] : i for i in range(len(num))} # dict로 만들어서 key, value로 저장
for i in range(len(arr)):
    print(res[arr[i]], end=" ")
