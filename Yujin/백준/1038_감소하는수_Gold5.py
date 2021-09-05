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
        if x <= tmp: # 해당 행에서 몇번째 순서에 해당하는지 확인
            start = start_num[index] + i # 헤딩 헹에서 처음 시작하는 숫자를 알아내고 찾은 열을 더해서 해당 행의 열에서 시작하는 숫자를 알아냄
                                         # N = 18이면 index = 2이고 x = 8, i = 3, start는 해당 행이 시작하는 숫자는 1이고 거기서 3만큼 떨어져있으니 18이 해당하는 행의 열의 처음 시작하는 숫자는 4
            a = num.index(start)
            all = []
            for nums in combinations(num[a:], index): # 숫자는 내림차순이어야 하므로 조합으로 배열에 저장
                all.append(nums)
            return all[len(all)-x] # 구한 숫자들을 모았을때 오름차순에서 뽑아야 하니까 구한 배열의 크기에서 해당 행의 index(열)을 빼면 원하는 숫자 집합이 나옴

if N > 1023:
    print(-1)
else:
    for i in range(1, 11):
        if N <= total[i]: # N=0일때는 여기서 total[0]에 걸리고 음의 index는 없으니까 N = N+1로 만들고 시작
            N -= total[i-1] # 해당 total의 행에서 순서를 0부터 비교할 수 있도록 이전 행의 총합을 빼줌
            result = getNum(N, i)
            for i in range(len(result)):
                print(result[i], end="")
            break
        
        