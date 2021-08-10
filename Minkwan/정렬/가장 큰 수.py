# 정렬Lv2 가장 큰 수 : https://programmers.co.kr/learn/courses/30/lessons/42746
# 다시 다 이해하고 올리기
# 접근1 : 문자는 첫글자가 큰순서대로, 문자열의 길이가 긴 순서대로 비교가 가능
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*3, reverse = True)  # 람다정렬은 이해가 여전히 잘 안됨........
    if sum(list(map(int, numbers))) == 0:
        answer = '0'
    else:
        answer = "".join(numbers)
    return answer


numbers1 = {6, 10, 2}
numbers2 = {3, 30, 34, 5, 9}

print(solution(numbers1))  # 6210
print(solution(numbers2))  # 9 5 34 3 3 0