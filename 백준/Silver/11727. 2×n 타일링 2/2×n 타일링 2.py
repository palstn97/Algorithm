# dp를 사용하는 문항 -> 점화식이니까
n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, 1001):
    dp[i] = 2 * dp[i - 2] + dp[i - 1]

res = dp[n] % 10007
print(res)