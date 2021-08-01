# 해시Lv3 베스트 앨범 : https://programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    # 접근 1 : 딕셔너리를 이용, 테스트통과 2/15 -> 좀더 효율적으로
    # 접근 2 : 람다정렬 적용결과, 테스트퇑과 3/15
    answer = []

    d_genres = {genres[0]: [(plays[0], 0)]}  # 전체정보를 담은 딕셔너리, key : 장르이름 -> value : 실행횟수, 고유번호
    sp_dic = {genres[0]: plays[0]}  # 플레이수 총합계산을 위한 딕셔너리, key : 장르이름 -> value : 플레이수

    for i in range(1, len(genres)):
        if genres[i] not in d_genres.keys(): # 딕셔너리.keys()는 key값을 배열로 반환해줌, 그 배열안에 장르 이름이 있는지 확인
            d_genres[genres[i]] = [(plays[i], i)]  # 없으면 새로운 genre를 key값으로 가지는 value 생성
            sp_dic[genres[i]] = plays[i]
        else:
            d_genres[genres[i]].append((plays[i], i))  # 있으면 기존에 있던 genre에 value 추가
            sp_dic[genres[i]] += plays[i]

    s_sp_dic = sorted(sp_dic, key=lambda x: x[1], reverse=True)  # sp_dic에서 x[1], 즉 플레이수 총합을 기준으로 내림차순 정렬
    # print(s_sp_dic)
    # print(d_genres)

    for i in s_sp_dic:
        play = d_genres[i]
        play = sorted(play, key=lambda x: (-x[0], x[1]))  # play에서 첫번째 인자(x[0],플레이수)는 내림차순 정렬후 두번째 인자(x[1],고유번호)는 오름차순
        for j in range(len(play)):
            if j == 2:
                break
            answer.append(play[j][1])

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))  # [4,1,3,0] 나와야함
