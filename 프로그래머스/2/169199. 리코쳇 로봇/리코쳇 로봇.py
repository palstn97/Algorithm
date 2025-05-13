from collections import deque


def solution(board):
    n, m = len(board), len(board[0])
    visited = [[0] * m for _ in range(n)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 시작 위치
    for r in range(n):
        for c in range(m):
            if board[r][c] == 'R':
                start_r, start_c = r, c
                break

    q = deque()
    q.append((start_r, start_c, 0))   # 이동 횟수
    visited[start_r][start_c] = 1

    while q:
        curr_r, curr_c, cnt = q.popleft()

        if board[curr_r][curr_c] == 'G':
            return cnt

        for dr, dc in dir:
            next_r, next_c = curr_r, curr_c

            while 0 <= next_r + dr < n and 0 <= next_c + dc < m and board[next_r + dr][next_c + dc] != 'D':
                next_r += dr
                next_c += dc

            if visited[next_r][next_c] == 0:
                visited[next_r][next_c] = 1
                q.append((next_r, next_c, cnt + 1))

    return -1