from collections import deque

def bfs(x, y, field, visited, M, N):
    # (x, y)에서 시작해서 연결된 모든 배추 방문 처리하기
    q = deque([(x, y)])
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        cx, cy = q.popleft()
        # 4방향 탐색
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 범위 안에 존재하고 배추가 있고 아직 방문 전이라면...
            if 0 <= nx < M and 0 <= ny < N:
                if field[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    # 배추밭
    field = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1

    worm = 0
    for i in range(M):
        for j in range(N):
            # 배추가 있고 아직 방문하지 않았다면
            if field[i][j] == 1 and not visited[i][j]:
                bfs(i, j, field, visited, M, N)
                worm += 1
    
    print(worm)