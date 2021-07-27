# 스택/큐 기능 개발 : https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    # 접근 1 : 걸리는 날짜를 계산하는 day 리스트를 선언하여 배열을 검색하여 결과 찾기 : 결과는 맞았지만 시간 초과
    answer = []
    day = []
    cnt = 1
    n = len(progresses)

    for i in range(0, n):
        dif = 100 - progresses[i]  # dif = [7, 70, 45] , [5, 10, 1, 1, 20, 1] 저장
        day_n = dif / speeds[i]
        day.append(day_n)  # day = [7, 2.3333, 9] , [5, 10, 1, 1, 20, 1]   첫값이 뒷값보다 크면 카운트 증가

    for i in range(0, n):
        if i == n - 1:
            answer.append(cnt)
            return answer
        elif day[i] >= day[i+1]:
            cnt += 1
            continue
        else:
            answer.append(cnt)
            cnt = 1

    return answer


progresses1 = [93, 30, 55]
speeds1 = [1, 30, 5]

progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = [1, 1, 1, 1, 1, 1]

print(solution(progresses1, speeds1))
print(solution(progresses2, speeds2))
