# 18870번 좌표 압축 : https://www.acmicpc.net/problem/18870

# 접근1 : set으로 만들어서 중복 제거후 다시 리스트로 만들어서 정렬후 인덱스값 넣어주기 -> 시간초과
# 접근2 : for문 안에서 바로 중복값 체크해서 위과정 반복 -> 시간초과
# 접근3 : ...?

n = int(input())

a = list(map(int, input().split()))
b = []
ans = []

for i in a:
    if i not in b:
        b.append(i)

b.sort()

for i in range(0, len(a)): # 오름차순된 na의 인덱스값이 좌표압축 갯수
    ans.append(b.index(a[i]))

for i in ans:
    print(i, end=' ')

