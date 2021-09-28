triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    dp = triangle[:]
    lenT = len(triangle)
    for i in range(1, lenT):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = dp[i-1][j-1] + dp[i][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j] if dp[i-1][j] + dp[i][j] > dp[i-1][j-1] + dp[i][j] else dp[i-1][j-1] + dp[i][j]

    return max(dp[lenT-1])

print(solution(triangle))