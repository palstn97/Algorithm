T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    rotate_90 = [[0] * N for _ in range(N)]
    rotate_180 = [[0] * N for _ in range(N)]
    rotate_270 = [[0] * N for _ in range(N)]

    for c in range(N):
        for r in range(N):
            rotate_90[r][N - c - 1] = matrix[c][r]
            rotate_180[N - c - 1][N - r - 1] = matrix[c][r]
            rotate_270[N - r - 1][c] = matrix[c][r]

    print(f"#{tc}")
    for c in range(N):
        print(''.join(list(map(str, rotate_90[c]))), end=' ')
        print(''.join(list(map(str, rotate_180[c]))), end=' ')
        print(''.join(list(map(str, rotate_270[c]))))