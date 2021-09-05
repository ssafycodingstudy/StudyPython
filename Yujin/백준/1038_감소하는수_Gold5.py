from itertools import combinations

N = int(input())
N += 1
start_num = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
dec = [[] for _ in range(11)]
dec[0] = [0]*11

for i in range(1, 11):
    dec[i].append(1)
    for j in range(1, 11-i):
        x = dec[i-1][j] + dec[i][j-1]
        dec[i].append(x)

total = [0]*11
total[0] = 0
for i in range(1, 11):
    total[i] = total[i-1] + sum(dec[i])

def getNum(x, index):
    tmp = 0
    for i in range(len(dec[index])):
        tmp += dec[index][i]
        if x <= tmp:
            start = start_num[index] + i
            a = num.index(start)
            all = []
            for nums in combinations(num[a:], index):
                all.append(nums)
            return all[len(all)-x]

if N > 1023:
    print(-1)
else:
    for i in range(1, 11):
        if N <= total[i]:
            N -= total[i-1]
            result = getNum(N, i)
            for i in range(len(result)):
                print(result[i], end="")
            break
        
        