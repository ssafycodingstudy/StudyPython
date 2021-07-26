def solution(participant, completion):
    # 접근1 : 2중 for문을 이용한 비교 : 너무 복잡함, 시간복잡도 높음
    # 접근2 : set으로 각각 리스트를 집합 : 이럴경우 중복된 내용이 사라져 3번에서 mislav가 인식이 안 됨
    # 접근3 : 정렬해서 비교 : 정렬해서 비교하는게 제일 간단하고 시간복잡도가 낮음을 확인
    answer = ""

    participant.sort()
    completion.sort()

    # print(participant)
    # print(completion)

    for i in range(len(completion)):  # 이렇게 비교할 경우 탈락자가 정렬의 맨 뒤에 있으면 answer가 비어버림
        if participant[i] != completion[i]:
            answer = participant[i]
            break  # break를 안걸어주면 for문이 계속 돌아 아주 비효율적, 그래서 틀림

    if answer == "":
        answer = participant[-1]  # 맨 뒤에값

    return answer  # 위의 if answer == ""를 쓰지 않을거라면 for안의 if문에서 answer을 반환하거나 해당 안할시 여기서 participant[-1]을 바로 반환시키기(유진님 방법)



participant1 = ["leo","kiki","eden"]
completion1 = ["eden","kiki"]

participant2 = ["marina","josipa","nikola","vinko","filipa"]
completion2 = ["josipa","filipa","marina","nikola"]

participant3 = ["mislav","stanko","mislav","ana"]
completion3 = ["stanko","ana","mislav"]

print(solution(participant1, completion1))
print(solution(participant2, completion2))
print(solution(participant3, completion3))
