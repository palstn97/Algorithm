T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0

    dir1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dir2 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for r in range(N):
        for c in range(N):
            sum_fly1 = matrix[r][c]
            for i in range(4):
                for a in range(1, M):
                    next_r = r + a * dir1[i][0]
                    next_c = c + a * dir1[i][1]
                    if 0 <= next_r < N and 0 <= next_c < N:
                        sum_fly1 += matrix[next_r][next_c]
            max_fly = max(max_fly, sum_fly1)
            
    for r in range(N):
        for c in range(N):
            sum_fly2 = matrix[r][c]
            for i in range(4):
                for a in range(1, M):
                    next_r2 = r + a * dir2[i][0]
                    next_c2 = c + a * dir2[i][1]
                    if 0 <= next_r2 < N and 0 <= next_c2 < N:
                        sum_fly2 += matrix[next_r2][next_c2]
            max_fly = max(max_fly, sum_fly2)
            
    print(f"#{tc} {max_fly}")