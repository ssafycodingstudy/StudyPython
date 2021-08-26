# 조이스틱 프로그래머스
def solution(name):
    alpha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    res = [0 for _ in range(len(name))]
    for i in range(len(name)):
        res[i]= alpha[(ord(name[i]) - ord("A"))]

    answer = 0
    index = 0
    while True:
        answer += res[index]
        res[index] = 0
        if sum(res) == 0:
            print(answer)
            return answer
        left, right = 1, 1
        while res[index - left] == 0:
            left += 1
        while res[index + right] == 0:
            right += 1
        
        answer += left if left < right else right
        index += -left if left < right else right