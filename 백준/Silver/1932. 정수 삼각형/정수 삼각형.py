n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * i for i in range(1, n + 1)] # 삼각형 구조와 일치시키기 위해서 i번째 줄은 (i+1)개의 원소를 가진다. 즉 dp[i][j]와 triangle[i][j]가 같은 위치에 존재
dp[0][0] = triangle[0][0]   # 초기값 설정 -> 꼭대기값으로 초기화

for i in range(1, n):   # 0번째 줄은 초기화 됐기 때문에 1부터 시작
    for j in range(i + 1):  # j는 0부터 i까지
        if j == 0:  # 왼쪽일 때
            dp[i][j] = dp[i-1][0] + triangle[i][j]
        elif j == i:    # 맨 오른쪽일 때
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:   # 중간의 경우 -> 중간이니까 j-1도 괜찮다!
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[n-1])) # dp는 0부터 시작하기 때문에 마지막 줄은 dp[n-1]