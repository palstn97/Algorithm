C, N = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

max_p = 0
for c, p in mat:
    if p > max_p:
        max_p = p
INF = float('inf')

# dp[i] = i명 정확히 모으는 최소 비용
dp = [INF] * (C + max_p + 1)
dp[0] = 0   # 초기값

for i in range(1, C+ max_p + 1):
    for c, p in mat:
        if i - p >= 0:
            dp[i] = min(dp[i], dp[i - p] + c)

# C 이상 중 최소 비용
print(min(dp[C:]))