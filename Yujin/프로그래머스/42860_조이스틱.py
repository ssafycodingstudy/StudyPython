# 조이스틱 프로그래머스
def solution(name):
    alpha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    res = [0 for _ in range(len(name))]
    cnt = 0
    for i in range(len(name)):
        res[i]= alpha[(ord(name[i]) - ord("A"))]
    answer = sum(res)

    size = len(name)
    lr = size - 1
    for i in range(size):
        index = i + 1
        while index < size and res[index] == 0:
            index += 1
        tmp = min(i, size - index)
        lr = min(lr, i + size - index + tmp)

    answer += lr
    print(answer)

solution("ABAAAAAAAAABB")