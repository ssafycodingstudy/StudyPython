triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    dp = triangle[:]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = dp[i-1][j-1] + dp[i][j]
            else:
                dp[i][j] = max(dp[i-1][j] + dp[i][j], dp[i-1][j-1] + dp[i][j])

    return max(dp[-1])

print(solution(triangle))