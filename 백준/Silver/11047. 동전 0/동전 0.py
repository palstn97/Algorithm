N, K = map(int, input().split())
coins = []

for i in range(N):
    coins.append(int(input()))

res = 0

# 그리디 사용할거니까 가장 큰 가치부터 생각
for j in range(N - 1, -1, -1):
    if K >= coins[j]:
        res += K // coins[j]
        K %= coins[j]   # 남은 금액
    if K == 0:
        break

print(res)