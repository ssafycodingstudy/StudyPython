import sys
input = sys.stdin.readline
t = int(input())


def isOne(s, start, end):
    check_one = True
    while start <= end:
        if s[start] == s[end]:
            start += 1
            end -= 1
            continue
        else:
            check_one = False
            break
    if check_one:
        return 1
    return 2


def isZero(s, start, end):
    while start <= end:
        if s[start] == s[end]:
            start += 1
            end -= 1
            continue
        else:
            start_check = isOne(s, start + 1, end)
            end_check = isOne(s, start, end - 1)
            if start_check == 1 or end_check == 1:
                return 1
            else:
                return 2
    return 0


for _ in range(t):
    check = False
    s = input().rstrip('\n')
    start = 0
    end = len(s) - 1
    answer = isZero(s, start, end)
    print(answer)
