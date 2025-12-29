from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if grid[r][c] == 2:
            arr_r, arr_c = r, c

# 거리(정답) 배열 초기화 -> 이때 -1은 아직 방문하지 않은 것. 아직 bfs로 탐색하지 않음
distance = [[-1] * M for _ in range(N)]

# 델타 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(R, C):
    q = deque([(R, C)]) # 시작지점을 q에 담아주고
    distance[R][C] = 0  # 목표지점까지는 자기 위치 그대로니까 0

    while q:
        x, y = q.popleft()
        # 델타 탐색 진행 -> 상하좌우 방향 탐색
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 1 and distance[nx][ny] == -1:    # 아직 탐색하지 않았고 갈 수 있는 길이라면
                    distance[nx][ny] = distance[x][y] + 1   # 다음 위치는 현재 위치보다 1증가
                    q.append((nx, ny))

bfs(arr_r, arr_c)   # bfs함수 실행

# 모든 지점 순회하면서 출력하기
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            print(0, end = ' ')
        else:
            print(distance[i][j], end = ' ')
    print() # 줄바꿈해주기