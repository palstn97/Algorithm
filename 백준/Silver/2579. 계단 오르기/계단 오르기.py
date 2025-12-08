N = int(input())
stairs = [0] * 301  # 계단 저장 -> 시작은 계단으로 포함 안하니까 301로 하기
for i in range(1, N + 1):
    stairs[i] = int(input())
# 점화식? dp인데 늘 어렵다
'''
DP 문제는
1. 점화식 먼저 세우고
2. 점화식이 참조하는 과거 값들을 확인하고
3. 그에 맞춰 초기값을 설정한다.
'''
# n번째 계단에 도착하는걸 생각해보면 우선 n-1번째에서 n번째로. 즉 1칸 올라오기이다. 이때 n-2번째를 밟았으면 이건 안됨
# n-2번째에서 바로 n번째로 올라오는거. 즉 2칸 올라오기

# DP 배열 -> 계산된 값!
dp = [0] * 301

# 초기값 설정
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, N + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[N])