def getSeq(index):
    # 숫자 넣기전에 좋은수열인지 확인
    for i in range(1, (index//2)+1):
        if seq[-i:] == seq[-2*i:-i]:
            return False

    # 모든 수가 채워질때
    if index == N:
        for i in range(N):
            print(seq[i], end="")
        return True
    
    # 1, 2, 3 숫자 넣기
    for i in range(1, 4):
        seq.append(i)
        if getSeq(index + 1) == True:
            return True
        seq.pop()

N = int(input())

seq = []
getSeq(0)