import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weight = [0]
value = [0]

for _ in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)

dp = [[0] * (K + 1) for _ in range(N + 1)]
# 초기값 설정은? 이미 0으로 아무것도 안 넣은 상태가 초기값으로 설정이 되어 있다. 그렇기에 직접 따로 설정을 하지는 않아도 된다!

for i in range(1, N + 1):
    for w in range(1, K + 1):
        if w < weight[i]:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i- 1][w], dp[i - 1][w - weight[i]] + value[i])

print(dp[N][K])