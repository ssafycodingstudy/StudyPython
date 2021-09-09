n = int(input())
result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def solution():
    x = 10
    while True:
        temp = str(x)
        # print(temp)
        check = True
        for i in range(1, len(temp)):
            if temp[i - 1] <= temp[i]:
                start = temp[:i - 1]
                mid = str(int(temp[i - 1]) + 1)
                end = '0' + temp[i + 1:]
                x = int(start + mid + end)
                check = False
                break
        if check:
            result.append(x)
            if x == 9876543210:
                return
            x += 1


if n <= 1022:
    solution()
    print(result[n])
else:
    print(-1)
