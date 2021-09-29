'''
의식의 흐름
1. 일단 삼각형을 문제의 그림 모양이 아니라 배열에 맞춰 삼각형 모양으로 바라보기
2. 파스칼 삼각형같은 느낌?
3. 처음에는 모든 합에 대한 값을 처리하기 위해 answer = math.pow(2, height-1) 를 해서 max값을 찾으려함 -> 아주 비효율적 및 처리 힘듬(dfs를 사용해야하나?)
4. 행의 맨 왼쪽값은 바로 위에껄 더하면됨, 행의 맨 오른쪽값은 왼쪽위에있는 값 더해주면됨
5. 가운데는 왼쪽위, 바로 위 2개에 대한 합이 나오는데 이중에서 더 큰값만 챙겨주면서 가면 기존의 triangle의 형태를 그대로 유지하며 갈 수 있음
'''
def solution(triangle):
    height = len(triangle)  # 삼각형의 높이

    for i in range(1, len(triangle)):  # 1부터 삼각형의 높이까지, 0일때는 어짜피 triangle의 제일 첫번째값 그대로 남아있음
        for j in range(len(triangle[i])):  # 각 행의 길이까지, 계단식 삼각형 2개,3개,4개 이렇게 늘어감
            if j == 0:
                triangle[i][j] += triangle[i-1][j]  # 행의 맨 왼쪽 값은 바로 위에꺼랑 더해주면됨
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]  # 행의 맨 오른쪽 값은 왼쪽 대각선 위랑 더해주면됨
            else:
                # 이렇게 처리해야 기존 triangle의 크기에 맞춰서 값을 저장시켜 나갈수 있음
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])  # 나머지는 파스칼 삼각형처럼 계산해서 더 큰값을 저장시키자자
    answer = max(triangle[-1])  # 제일 마지막 행에서의 최댓값
    return answer


triangle = [[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]

print(solution(triangle))