'''
bfs로 돌면서 같은 색상이면 연결된 구역의 개수를 세면서 구역을 유지하기.
만약 다른 색상이면 다른 색상으로 저장하고 계속 탐색을 지속할 것
델타 탐색을 사용하기
색맹 버전이랑 정상인 버전으로 나눠서 하기
'''
from collections import deque

N = int(input())
grid = [list(map(str, input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(target_grid):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    # (0, 0)에서 시작을 하면 (0, 0)과 연결된 구역 1개만 찾기 때문에 q에 나중에 담아주자

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                # 여기서부터 bfs 시작하기
                color = target_grid[r][c]
                q = deque([(r, c)])
                visited[r][c] = True

                while q:
                    x, y = q.popleft()

                    for i in range(4):
                        next_x = x + dr[i]
                        next_y = y + dc[i]
                        if 0 <= next_x < N and 0 <= next_y < N:
                            if not visited[next_x][next_y] and target_grid[next_x][next_y] == color:
                                visited[next_x][next_y] = True
                                q.append((next_x, next_y))

                cnt += 1

    return cnt

normal = bfs(grid)

# R -> G로 변환하기
grid2 = [['G' if c == 'R' else c for c in r] for r in grid]
blind = bfs(grid2)

print(normal, blind)