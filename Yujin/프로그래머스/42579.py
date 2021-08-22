# 베스트 앨범 - 프로그래머스
from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre = defaultdict(lambda: 0)
    total = defaultdict(lambda: [])

    # genre에 각 장르마다 재생된 수 더하기
    # total에 장르별로 (재생된 수, 고유번호) 추가하기
    for i in range(len(genres)):
        genre[genres[i]] += plays[i]
        total[genres[i]].append((plays[i], i))

    genre = sorted(genre.items(), key = lambda x:x[1], reverse = True)

    for i in total:
        total[i] = sorted(total[i], key = lambda x:x[0], reverse = True)[:2]

    while len(genre) > 0:
        maxx = genre.pop(0) # genre 맨앞이 최대
        for i in total: 
            if i == maxx[0]: # total에서 최대값과 같은 수와 장르를 가지고 있다면
                if len(total) > 1: #장르에서 재생된 노래가 2개이면
                    answer.append(total[i][0][1])
                    answer.append(total[i][1][1])
                else: # 장르에서 재생된 노래가 1개이면
                    answer.append(total[i][0][1])
    return answer

    