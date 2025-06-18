N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]   # dp[a][b]는 길이가 a고 b는 가장 마지막 숫자
for i in range(1, 10):
    dp[1][i] = 1    # 한 자리 수는 1~9가 가능 -> 1로 만들어주기

num = 1000000000

for j in range(2, N + 1):   # 앞에서 한 자리수는 처리 했으니까 2부터 시작
    for k in range(10):
        if k == 0:  # 0인 경우
            dp[j][k] = dp[j - 1][1] # 무조건 앞자리는 1이어야지만 k에 0이 올 수 있음
        elif k == 9:    # 9인 경우
            dp[j][k] = dp[j - 1][8] # 무조건 그 앞의 수는 8이어야지만 k에 9가 올 수 있음
        else:
            dp[j][k] = dp[j - 1][k - 1] + dp[j - 1][k + 1]  # 그 외에는 앞자리가 k-1도 되고 k+1도 된다.

print(sum(dp[N]) % num)