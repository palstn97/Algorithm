'''
기존의 bfs는 하나만 큐에 담았다면 이 문제는 동시에 익기 때문에 익은 토마토들을 모두 담아줘야한다.
함수 변수는 굳이 필요 없을거 같고 그냥 안에서 처리해도 무방!
델타 탐색으로 안익은 토마토 찾아서 익히고 날짜 +1 한 상태로 큐에 담아줄것.
'''
from collections import deque

def bfs():
    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque()

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append((i, j, 0))

    ripe_day = 0

    while q:
        x, y, day = q.popleft()
        ripe_day = max(ripe_day, day)   # 가장 마지막에 익은 토마토의 날짜가 필요하기 때문에!

        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = 1
                q.append((nx, ny, day + 1))

    # 안 익은 토마토 확인하기
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
    return ripe_day

print(bfs())