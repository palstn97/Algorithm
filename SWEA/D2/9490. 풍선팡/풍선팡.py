def balloon(mat):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_flower = 0
    for r in range(N):
        for c in range(M):
            flower_sum = mat[r][c]
            curr_r, curr_c = r, c
            for i in range(4):
                for j in range(1, mat[r][c] + 1):
                    next_r = curr_r + j * dir[i][0]
                    next_c = curr_c + j * dir[i][1]
                    if 0 <= next_r < N and 0 <= next_c < M:
                        flower_sum += mat[next_r][next_c]
                        max_flower = max(max_flower, flower_sum)

    return max_flower


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {balloon(matrix)}")