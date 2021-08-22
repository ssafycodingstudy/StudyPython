# 완전탐색 소수 찾기 : https://programmers.co.kr/learn/courses/30/lessons/42839

# 접근 1 : 종이조각으로 만들수있는 최대 숫자를 찾은후, 그 아래의 소수를 찾아보기?


from itertools import permutations  # 이런게 있다니;


def solution(numbers):
    answer = []
    nums = [n for n in numbers]  # numbers를 하나씩 잘라서 넣어줌
    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i))  # i개씩 순열조합 -> 근데 순열이랑 부분집합이랑 차이가 공집합이 있고없고차이?
    print(nums)
    print(per)
    return answer


numbers1 = "17"
numbers2 = "011"

a = []

print(solution(numbers1))  # 3 출력
print(solution(numbers2))  # 2 출력