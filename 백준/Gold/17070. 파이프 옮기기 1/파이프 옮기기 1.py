'''
DP인 이유?
- 큰 문제를 작은 부분 문제로 나눌 수 있다.
- 부분 문제의 답을 재사용할 수 있어야 한다.
파이프는 두 칸을 차지하고, 파이프 끝의 위치로 상태를 표현한다.
dp[3][4][가로] = (3, 4)에 가로 방향으로 도착하는 경우의 수
이건 어디서 올 수 있는가??
-> dp[3][3][가로]에서 오른쪽으로 (가로 -> 가로)
-> dp[2][3][대각선]에서 오른쪽으로 (대각선 -> 가로)
'''
import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j][방향] = (i, j)에 특정 방향으로 도착하는 경우의 수 / 방향: 0 = 가로, 1 = 세로, 2 = 대각선
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
# 초기값: (0, 1)에 가로 방향으로 시작하기
dp[0][1][0] = 1

for i in range(N):
    for j in range(N):
        # 벽이면 넘어가기
        if grid[i][j] == 1:
            continue

        # 가로로 도착했을 때, 즉 왼쪽에서 오른쪽으로
        if j > 0:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
        # 세로로 도착했을 때, 즉 위에서 아래로
        if i > 0:
            dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        # 대각선으로 도착했을 때
        if i > 0 and j > 0:
            # 3칸 모두 비어있어야 한다.
            if grid[i-1][j] == 0 and grid[i][j-1] == 0:
                dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])