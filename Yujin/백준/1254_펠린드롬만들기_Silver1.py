import sys
input = sys.stdin.readline

S = list(input().strip())
dp = []
for i in range(len(S)):
    R = []
    for j in range(len(S)-1, i-1, -1): # 앞에서 부터 하나씩 줄여나감
        R.append(S[j])
    if S[i:len(S)] == R[:len(S)]: # 펠린드롬인것을 찾으면
        dp = S[:i] # 펠린드롬 아닌 부분을 저장
        break
dp.reverse()
S = S + dp # 주어진 문자열에 펠린드롬 아닌 부분을 더함
print(len(S))

# 더 간단한 방법 72ms
S = input()
for i in range(len(S)):
    if S[i:] == S[i:][::-1]:
        print(len(S)+i)
        break