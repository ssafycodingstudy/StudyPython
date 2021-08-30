# 가장 큰 수  - 프로그래머스

def solution(numbers):
    numbers = list(map(str, numbers)) # 문자열로 비교
    numbers.sort(key=lambda x:x*3, reverse=True) # 원소가 1000이하이기 때문에 *3으로 자릿수를 늘려서 비교
    return str(int(''.join(numbers))) # 0000을 0으로 바꿔주기 위해서 str(int())