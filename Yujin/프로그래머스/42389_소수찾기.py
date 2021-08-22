from itertools import permutations
import math

# 소수인지 아닌지 분별
def decimal(a): 
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

def solution(numbers):
    answer = set([]) # 중복된 수 못들어가게 set

    for i in range(1, len(numbers)+1):
        for k in permutations(numbers, i):
            num = int(''.join(k))
            if decimal(num):
                answer.add(num)
    return len(answer)