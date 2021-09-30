def getT(i, j):
    tmp = 0
    index = 1
    if j < 1:
        for k in range(j, j+i):
            tmp += tHash[k]*(5**(i-index))
            index += 1
    elif j >= 1:
        tmp = 5*(getT(i, j-1) - tHash[j-1]*(5**(i-1))) + tHash[i+j-1]
    return tmp

def findString():
    for i in range(tLen-1, 1, -1):
        for j in range(tLen-i):
            tmp = 0
            tmp = getT(i, j)
            for k in range(j+1, tLen-i):
                tmp2 = getT(i, k)            
                if tmp == tmp2:
                    print(i)
                    return
    print(0)
    return

L = int(input())
text = input()
tHash = []
tLen = len(text)

for i in range(tLen):
    tHash.append(ord(text[i]))

findString()