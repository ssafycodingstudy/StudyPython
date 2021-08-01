# 해시Lv3 베스트 앨범 : https://programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    # 접근 1 : 딕셔너리를 이용, 테스트통과 2/15 -> 좀더 효율적으로

    answer = []
    dict_list = []

    d_genres = {genres[0]: [(plays[0], 0)]}  # 전체정보를 담은 딕셔너리, key : 장르이름 -> value : 실행횟수, 고유번호
    sp_dic = {genres[0]: plays[0]}  # 플레이수 총합계산을 위한 딕셔너리, key : 장르이름 -> value : 플레이수

    for i in range(1, len(genres)):
        if genres[i] not in d_genres.keys(): # 딕셔너리.keys()는 key값을 배열로 반환해줌, 그 배열안에 장르 이름이 있는지 확인
            d_genres[genres[i]] = [(plays[i], i)]  # 없으면 새로운 genre를 key값으로 가지는 value 생성
            sp_dic[genres[i]] = plays[i]
        else:
            d_genres[genres[i]].append((plays[i], i))  # 있으면 기존에 있던 genre에 value 추가
            sp_dic[genres[i]] += plays[i]

    s_sp_dic = sorted(sp_dic.items(), reverse=True)  # genres별 플레이수 총합이 내림차순으로 정렬

    for i in s_sp_dic:
        play = sorted(d_genres[i[0]], reverse=True)  # play안에 2차원배열 형태로 key값(i)의 value 저장
        for j in range(len(play)):
            if j == 2:  # 2개씩만 넣어야함
                break
            answer.append(play[j][1])

    # print(d_genres)
    # print(sp_dic)
    # print(s_sp_dic)
    # print(play)

    return answer

"""
속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
"""

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))  # [4,1,3,0] 나와야함
