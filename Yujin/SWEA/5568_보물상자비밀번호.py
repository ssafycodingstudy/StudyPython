T = int(input())
rotate = [0, 0, 2, 3, 4, 5, 6, 7]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    treasure = input()

    result = set()
    rot = rotate[N//4]
    for i in range(rot):
        for j in range(0, len(treasure), rot):
            result.add(int(treasure[j:j+rot], 16))

        treasure = treasure + treasure[0]
        treasure = treasure[1:]

    result = list(result)
    result.sort(reverse=True)
    print("#%d %d" %(tc,result[K-1]))