# 스택/큐 기능 개발 : https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    # 접근 1 : 걸리는 날짜를 계산하는 day 리스트를 선언하여 배열을 검색하여 결과 찾기 : 결과는 맞았지만 시간 초과
    # 접근 2 : day 리스트에 날짜를 저장하고 0번 인덱스만 참조하면서 pop으로 날려버리기 : 결과는 맞았지만 딱 1번 케이스에 대하여 시간 초과
    # 접근 3 : 앞에있던 day 리스트를 만드는 for문을 없애면 더 빨라지지 않을까? 접근2와 같은 방식이지만 조금더 간략화 : 성공
    answer = []
    cnt = 0
    day = 0

    while len(progresses) > 0:
        if (progresses[0] + speeds[0] * day) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)

    return answer


progresses1 = [93, 30, 55]
speeds1 = [1, 30, 5]

progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = [1, 1, 1, 1, 1, 1]

print(solution(progresses1, speeds1))
print(solution(progresses2, speeds2))
