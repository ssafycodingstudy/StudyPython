from copy import deepcopy
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def solution(triangle):
    dp = deepcopy(triangle)
    for i in range(1, len(dp)):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j] + dp[i][j], dp[i - 1][j - 1] + dp[i][j])
    answer = max(dp[-1])
    return answer


print(solution(triangle))
