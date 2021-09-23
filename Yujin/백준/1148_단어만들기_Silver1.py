import sys
input = sys.stdin.readline

N = input().strip()
arr = [[0]*26 for _ in range(200000)]
idx = 0
while N != "-": 
    for i in N: # 각 단어에서 사용한 알파벳 사용 횟수 저장
        arr[idx][ord(i)-65] += 1
    idx += 1
    N = input().strip()
    
M = input().strip()
while M != "#":
    puzzle = [0]*26
    answer = [0]*26
    for i in M: # puzzle에 있는 알파벳 사용 횟수 저장
        puzzle[ord(i)-65] += 1
    
    for i in range(idx):
        find = True
        for j in range(26):
            if arr[i][j] > puzzle[j]: # puzzle에 있는 횟수보다 많으면 탈락
                find = False
                break
        if find:
            for j in range(26):
                if arr[i][j] > 0: answer[j] += 1 # puzzle에 있는 알파벳이 몇개의 단어에서 사용되었는지 저장

    minV = 987654321
    maxV = 0
    minK = []
    maxK = []

    for i in range(26):
        if answer[i] != 0: 
            minV = min(minV, answer[i])
        if answer[i] == 0 and puzzle[i] > 0: # puzzle 가운데에 있을때 어떤 단어도 만들 수 없는 경우
            minV = 0
        maxV = max(maxV, answer[i])

    for i in range(26):
        if minV != 0 and minV == answer[i]:
            minK.append(chr(i+65))
        elif minV == 0 and puzzle[i] > 0 and answer[i] == 0: # 만들 수 있는 단어는 0이지만 puzzle가운데에 위치해 있을때
            minK.append(chr(i+65))
        if maxV == answer[i] and puzzle[i] > 0:
            maxK.append(chr(i+65))
    print(''.join(sorted(minK)), minV, ''.join(sorted(maxK)), maxV)
    M = input().strip()
    
 