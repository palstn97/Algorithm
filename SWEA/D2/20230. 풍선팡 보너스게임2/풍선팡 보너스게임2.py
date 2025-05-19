T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sum_balloon = 0
    lst = []

    for r in range(N):
        for c in range(N):
            sum_balloon = matrix[r][c]
            for i in range(4):
                for a in range(1, N):
                    next_r = r + a * dir[i][0]
                    next_c = c + a * dir[i][1]
                    if 0 <= next_r < N and 0 <= next_c < N:
                        sum_balloon += matrix[next_r][next_c]
            lst.append(sum_balloon)

    print(f"#{tc} {max(lst)}")