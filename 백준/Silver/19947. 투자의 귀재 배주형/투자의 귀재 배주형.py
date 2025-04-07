H, Y = map(int, input().split())
dp = [0] * (Y + 1)  # dp[0]부터 dp[Y]까지 저장 -> 총 Y + 1칸
dp[0] = H   # dp[i] -> i년 후 가질 수 있는 최대 금액을 지정 -> 시작할 때는 H원(0년차)

for i in range(1, Y + 1):
    if i >= 5:  # 5년 예금도 가능한 경우
        dp[i] = max(dp[i - 1] * 1.05, dp[i - 3] * 1.20, dp[i - 5] * 1.35)   # 가장 큰 금액 선택
    elif i >= 3:
        dp[i] = max(dp[i - 1] * 1.05, dp[i - 3] * 1.20)
    else:
        dp[i] = dp[i - 1] * 1.05
    dp[i] = int(dp[i])  # 소수점 버리고 정수 출력
# 이전 계산 결과를 활용하여 최적의 선택만 누적하기. 핵심은 이전 값을 저장해서 사용
print(int(dp[Y]))   # Y년 후 가장 많은 돈 출력