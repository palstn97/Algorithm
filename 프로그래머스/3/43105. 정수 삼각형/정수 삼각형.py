def solution(triangle):
    n = len(triangle)
    dp = [[0] * (len(triangle[i])) for i in range(n)]
    dp[0][0] = triangle[0][0]   # 초기값
    
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + triangle[i][j])
            if j < len(triangle[i - 1]):
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i][j])
        
    answer = max(dp[-1])
    return answer