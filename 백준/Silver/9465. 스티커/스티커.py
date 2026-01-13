'''
스티커를 떼면 상하좌우 스티커를 사용하지 못 함.
대각선 방향으로만 이동이 가능하고 점수 최대화가 목표!
이전 선택이 현재 선택에 영향을 미치고 각 위치에서 선택하거나 선택하지 않으면서 최댓값을 구하기 때문에 dp 문제이다.
dp[i][j] = i행 j열의 스티커를 선택했을 때 얻을 수 있는 최대 점수
'''
T = int(input())
for t in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    
    dp = [[0] * n for _ in range(2)]

    # 초기값 설정
    dp[0][0] = sticker[0][0]    # 위쪽 첫 번째 스티커
    dp[1][0] = sticker[1][0]    # 아래쪽 첫 번째 스티커

    for j in range(1, n):
        if j == 1:  # j가 1인 경우에는 무조건 바로 전 대각선에서만 올 수 있기 때문에 따로 처리를 해준다.
            dp[0][j] = dp[1][j - 1] + sticker[0][j]
            dp[1][j] = dp[0][j - 1] + sticker[1][j]
        else:   # 왜 j + 1이 아니라 j - 2가 오냐면 dp 문제는 언제나 왼쪽에서 오른쪽으로 진행한다. 즉 이전의 값으로 결정을 하는거지 이후의 값으로 결정하는게 아니다!
            dp[0][j] = max(dp[1][j - 1], dp[1][j - 2]) + sticker[0][j]
            dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + sticker[1][j]

    print(max(dp[0][n-1], dp[1][n-1]))