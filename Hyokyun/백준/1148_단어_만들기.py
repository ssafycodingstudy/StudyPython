import sys
input = sys.stdin.readline
word = list(input().rstrip())
arr = []
while word[0] != '-':
    arr.append(word)
    word = list(input().rstrip())
    if word[0] == '-':
        break
puzzle = list(input().rstrip())
while puzzle[0] != '#':
    puzzle.sort()
    dic = {}
    dic_count = {}
    for i in range(len(puzzle)):
        dic_count[puzzle[i]] = 0
    for i in range(len(arr)):
        for k in range(len(puzzle)):
            dic[puzzle[k]] = 0
        for k in range(len(puzzle)):
            dic[puzzle[k]] += 1
        check = False
        for j in arr[i]:
            if (j in puzzle) and dic[j] != 0:
                dic[j] -= 1
            else:
                check = True
                break
        if not check:
            for k in set(arr[i]):
                dic_count[k] += 1
    maxValue = max(dic_count.values())
    minValue = min(dic_count.values())
    for i in dic_count.keys():
        if dic_count[i] == minValue:
            print(i, end='')
    print(" ", end='')
    print(minValue, end='')
    print(" ", end='')
    for i in dic_count.keys():
        if dic_count[i] == maxValue:
            print(i, end='')
    print(" ", end='')
    print(maxValue)
    puzzle = list(input().rstrip())
    if puzzle[0] == '#':
        break
