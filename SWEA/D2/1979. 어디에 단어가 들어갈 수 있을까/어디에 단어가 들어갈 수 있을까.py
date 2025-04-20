def word(mat):
    total = 0

    # 가로 줄 검사
    for r in range(N):
        for c in range(N - K + 1):
            if mat[r][c:c + K] == [1] * K:
                # 양 옆이 벽이거나 경계라면 카운트
                if (c == 0 or mat[r][c - 1] == 0) and (c + K == N or mat[r][c + K] == 0):
                    total += 1

    # 세로 줄 검사
    for c in range(N):
        for r in range(N - K + 1):
            line = [mat[r + i][c] for i in range(K)]
            if line == [1] * K:
                if (r == 0 or mat[r - 1][c] == 0) and (r + K == N or mat[r + K][c] == 0):
                    total += 1

    return total


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = word(matrix)
    print(f"#{tc} {result}")