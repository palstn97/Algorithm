T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    dir1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dir2 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for r in range(N):
        for c in range(N):
            sum_fly1 = matrix[r][c]
            for i in range(4):
                for a in range(1, M):
                    next_r1 = r + a * dir1[i][0]
                    next_c1 = c + a * dir1[i][1]
                    if 0 <= next_r1 < N and 0 <= next_c1 < N:
                        sum_fly1 += matrix[next_r1][next_c1]
            lst.append(sum_fly1)
            sum_fly2 = matrix[r][c]
            for j in range(4):
                for b in range(1, M):
                    next_r2 = r + b * dir2[j][0]
                    next_c2 = c + b * dir2[j][1]
                    if 0 <= next_r2 < N and 0 <= next_c2 < N:
                        sum_fly2 += matrix[next_r2][next_c2]
            lst.append(sum_fly2)
    print(f"#{tc} {max(lst)}")