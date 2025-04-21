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

# 조금 더 괜찮은 풀이
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for c in range(N):
        count = 0   # 문자열 길이 세기
        # 행 우선
        for r in range(N):
            if matrix[c][r] == 1:
                count += 1
            if (matrix[c][r] == 0) or (r == N - 1): # 벽을 만나거나 0을 만나면 끝내는데
                if count == K:  # 이 시점에서 count가 K라면
                    result += 1 # result를 1 더해주기
                count = 0   # 그리고 count 초기화
        for r in range(N):
            if matrix[r][c] == 1:   # 열 우선
                count += 1
            if matrix[r][c] == 0 or r == N - 1:
                if count == K:
                    result += 1
                count = 0
    print(f"#{tc} {result}")
