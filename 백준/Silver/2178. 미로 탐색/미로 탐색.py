from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0, 1)])   # 거리를 계속 합해야하니까 (x, y, 거리) 이렇게 해야할듯?
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while q:
        curr_r, curr_c, result = q.popleft()

        # 만약 목표 지점에 도달하면 현재까지 합산된 거리 리턴해주기
        if curr_r == N - 1 and curr_c == M - 1:
            return result
        
        # 델타 탐색 사용
        for i in range(4):
            next_r = curr_r + dr[i]
            next_c = curr_c + dc[i]

            if 0 <= next_r < N and 0 <= next_c < M:
                if not visited[next_r][next_c] and maze[next_r][next_c] == 1:
                    visited[next_r][next_c] = True
                    q.append((next_r, next_c, result + 1))

print(bfs())