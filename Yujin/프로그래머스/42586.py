# 기능 개발 - 프로그래머스

def solution(progresses, speeds):
    answer = []
    day = 0
    cnt = 0
    
    #Queue FIFO 이용
    while len(progresses) > 0: 
        if (progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else: #100보다 크거나 같을때까지 계속 day + 1
            if cnt > 0:
                answer.append(cnt) # 앞에 기능보다 더 빨리 완료한 기능들 넣기
                cnt = 0
            day += 1
    answer.append(cnt)
    return answer