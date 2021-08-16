import itertools
def solution(numbers):
    arr = []
    arr2 = []
    prime = set()
    num = ""
    for i in range(len(numbers)):
        arr.append(numbers[i])
    for i in range(1, len(arr) + 1):
        temp = list(itertools.permutations(arr, i))
        for j in range(len(temp)):
            flag = False
            result = int("".join(temp[j]))
            for k in range(2, result):
                if result % k == 0:
                    flag = True
                    break
            if not flag and result > 1:
                prime.add(result)
    answer = len(prime)
    return answer