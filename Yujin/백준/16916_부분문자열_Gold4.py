S = input()
P = input()
sLen = len(S)
pLen = len(P)

pi = [0]*pLen
j = 0
for i in range(1, pLen):
    while j > 0 and P[i] != P[j]:
        j = pi[j-1]
    if P[i] == P[j]:
        j += 1
        pi[i] = j

cnt = 0
j = 0
for i in range(sLen):
    while j > 0 and S[i] != P[j]:
        j = pi[j-1]
    if S[i] == P[j]:
        if j == pLen-1:
            cnt += 1
        else:
            j += 1
            
if cnt > 0:
    print(1)
else:
    print(0)