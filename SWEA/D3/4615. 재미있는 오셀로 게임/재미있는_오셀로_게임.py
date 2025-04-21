T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [[0] * N for _ in range(N)]
    # 초기 돌 배치
    grid[N // 2 - 1][N // 2 - 1] = 2
    grid[N // 2][N // 2] = 2
    grid[N // 2 - 1][N // 2] = 1
    grid[N // 2][N // 2 - 1] = 1

    for _ in range(M):
        r, c, stone = list(map(int, input().split()))
        curr_r = r - 1
        curr_c = c - 1

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]    # 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하

        for i in range(8):
            next_r = curr_r + dir[i][0]
            next_c = curr_c + dir[i][1]

            flip = []
            while 0 <= next_r < N and 0 <= next_c < N:
                if grid[next_r][next_c] == 0:   # 빈칸이라면 더 이상 뒤집을 수 없다.
                    break   # 중간에 빈칸이 있다면 뒤집기를 할 수 없기 때문
                elif grid[next_r][next_c] == stone: # 만약 내 돌이 나온다면
                    for fr, fc in flip: # 그 사이에 있던 모든 상대돌들을 뒤집을 수 있다.
                        grid[fr][fc] = stone
                    break   # 한 방향 탐색이 끝났고 다른 방향으로 넘어가기
                else:   # 상대 돌일 경우
                    flip.append((next_r, next_c))   # flip에 담아주기
                next_r += dir[i][0]
                next_c += dir[i][1] # 다음 방향 탐색
        grid[curr_r][curr_c] = stone    # 탐색을 먼저하고 돌을 놓기! -> 먼저 돌을 넣는다면 탐색에 방해가 된다.

    b_cnt, w_cnt = 0, 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                w_cnt += 1
            elif grid[i][j] == 1:
                b_cnt += 1
    print(f"#{tc} {b_cnt} {w_cnt}")