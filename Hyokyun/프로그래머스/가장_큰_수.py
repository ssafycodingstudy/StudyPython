# numbers = [70, 3, 30, 34, 5, 9, 101, 102, 109, 98, 901, 0, 89]
# numbers = [89, 90, 9]
# numbers = [4, 41, 44, 45, 449]
# numbers = [0, 0, 0, 0]
# numbers.sort(key=lambda x: (-(x / (10 ** (len(str(x)) - 1))), len(str(x))))


def solution(numbers):
    numbers.sort(reverse=True, key=lambda x: (str(x) * 4))
    answer = ''
    for i in range(len(numbers)):
        answer += str(numbers[i])
    return str(int(answer))

print(solution(numbers))
