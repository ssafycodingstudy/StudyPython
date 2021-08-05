genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    sumGenres = {}
    songs = {}
    for i in range(len(genres)):
        sumGenres[genres[i]] = sumGenres.get(genres[i], 0) + plays[i]
    for i in range(len(genres)):
        songs[i] = [sumGenres[genres[i]], plays[i]]
    songs = sorted(songs.items(), key=lambda x: x[1], reverse=True)

    sumGenres = sorted(sumGenres.items(), key=lambda x: x[1], reverse=True)


    print(songs)
    print(sumGenres)
    return answer

solution(genres, plays)