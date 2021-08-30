# 힙Lv3 이중우선순위큐 : https://programmers.co.kr/learn/courses/30/lessons/42628

# 접근 1 : 각 operations의 문자열에서 첫글자를 확인, I이면 뒤에 숫자 append, D이면 뒤에 숫자 1인지 -1인지 확인 후 처리-> 성공!
def solution(operations):
    answer = []
    for i in operations:
        a, b = i.split(" ")  # 공백을 기준으로 왼쪽의 문자는 a로, 오른쪽의 문자열은 b로 들어감
        if a == "I":
            answer.append(int(b))
        else:
            if len(answer) > 0:  # 값이 들어가있어야 pop이 가능
                if b == "1":
                    answer.pop()  # 제일 오른쪽값 pop
                else:  # b가 -1 일때
                    answer.pop(0)  # 제일 왼쪽값 pop
            else:  # 값이 아무것도 없으면 pop하지말구 지나가!
                pass
        answer.sort()  # 정렬을 해줘야 그때그때 최솟값이 왼쪽, 최댓값이 오른쪽으로 가있음
        print(answer)
        
    if len(answer) == 0:  # 비어있을대 처리 안해주면 오류남 out or range
        return [0, 0]
    else:
        return [answer[len(answer)-1], answer[0]]


operations1 = {"I 16", "D 1"}
operations2 = {"I 7", "I 5", "I -5", "D -1"}

print(solution(operations1))
print(solution(operations2))