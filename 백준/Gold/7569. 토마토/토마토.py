from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]   # 3차원 배열 입력받기

def tomato():
    q = deque()
    for h in range(H):  # 높이
        for r in range(N):  # 세로
            for c in range(M):   # 가로
                if box[h][r][c] == 1:
                    q.append((h, r, c, 0))

    # 6방향 -> 3차원이니까
    dh = [1, -1, 0, 0, 0, 0]
    dr = [0, 0, 1, -1, 0, 0]
    dc = [0, 0, 0, 0, 1, -1]

    days = 0

    while q:
        h1, r1, c1, day = q.popleft()
        days = max(days, day)

        for i in range(6):
            nh = h1 + dh[i]
            nr = r1 + dr[i]
            nc = c1 + dc[i]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
                if box[nh][nr][nc] == 0:
                    box[nh][nr][nc] = 1
                    q.append((nh, nr, nc, day + 1))

    # 익지않은 경우 발생시 -1 반환
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if box[h][r][c] == 0:
                    return -1
                
    return days

print(tomato())