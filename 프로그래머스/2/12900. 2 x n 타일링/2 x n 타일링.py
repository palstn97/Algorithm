# 피보나치 수열 -> dp 사용해서 해결해보기
def solution(n):
    mod = 1000000007
    dp = [0] * (n + 1)
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    answer = dp[n]
    return answer