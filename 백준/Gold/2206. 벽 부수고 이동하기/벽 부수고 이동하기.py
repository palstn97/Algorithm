from collections import deque
# import sys
# input = sys.stdin.readline

def bfs():
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]   # 3차원 행렬 -> visited[r][c][broken] = 방문여부 broken이 0이면 벽 안부수고 (r, c)방문 여부, 1이면 벽 부수고 방문 여부
    q = deque([(0, 0, 0, 1)])   # (r, c, broken, 거리) -> 거리는 현재 위치도 포함이니까 일단 1부터 시작! 그리고 벽 안부쉈으니까 0
    visited[0][0][0] = True # 시작점 방문처리. broken = 0인 상태로 (0, 0) 방문했다고 표시

    while q:
        r, c, broken, dist = q.popleft()
        if r == N - 1 and c == M - 1:   # (N, M)에 도달했을 때 -> (1, 1)에서 시작임. 그니까 (0, 0)이 사실은 (1, 1)인 것이다.
            return dist
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if grid[nr][nc] == 0: # 빈 칸인 경우
                    if not visited[nr][nc][broken]: # broken 상태 그대로 유지하면서 이동하기. 벽을 안 부쉈으면 계속 0이고 부쉈으면 계속 1이다.
                        visited[nr][nc][broken] = True
                        q.append((nr, nc, broken, dist + 1))
                elif grid[nr][nc] == 1 and broken == 0: # 벽인데 아직 안 부쉈다면? 아직 기회가 있다..! 벽을 부수고 진입하고 broken이 0에서 1로 변경되고 이후로는 벽을 더 못 부순다.
                    if not visited[nr][nc][1]:  # broken이 1이면 이미 벽을 부쉈으니까 벽 통과가 불가능하다.
                        visited[nr][nc][1] = True
                        q.append((nr, nc, 1, dist + 1))

    return -1

N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
ans = bfs()
print(ans)