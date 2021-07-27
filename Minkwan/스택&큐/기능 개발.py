# 스택/큐 기능 개발 : https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    # 접근 1 : 걸리는 날짜를 계산하는 day 리스트를 선언하여 배열을 검색하여 결과 찾기 : 결과는 맞았지만 시간 초과
    # 접근 2 : day 리스트에 날짜를 저장하고 0번 인덱스만 참조하면서 pop으로 날려버리기 : 결과는 맞았지만 딱 1번 케이스에 대하여 시간 초과
    answer = []
    day = []
    cnt = 0
    n = len(progresses)

    for i in range(0, n):
        day_n = (100 - progresses[i]) / speeds[i]  # dif = [7, 70, 45] , [5, 10, 1, 1, 20, 1] 저장
        day.append(day_n)  # day = [7, 2.3333, 9] , [5, 10, 1, 1, 20, 1]   첫값이 뒷값보다 크면 카운트 증가

    long_t = day[0]  # 제일 오래걸리는 시간 = 일단 첫번째값

    while len(day) > 0:
        if long_t >= day[0]:
            day.pop(0)
            cnt += 1
        else:
            answer.append(cnt)
            long_t = day[0]
            cnt = 0
    answer.append(cnt)

    return answer


progresses1 = [93, 30, 55]
speeds1 = [1, 30, 5]

progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = [1, 1, 1, 1, 1, 1]

print(solution(progresses1, speeds1))
print(solution(progresses2, speeds2))
