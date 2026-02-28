import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

cleaner = []    # 공기청정기
for i in range(R):
    if room[i][0] == -1:
        cleaner.append(i)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solve(grid):
    top = cleaner[0]
    bot = cleaner[1]

    # 미세먼지 확산
    new_grid = [row[:] for row in grid] # 원본 복사해서 원본에는 확산량 계산하고 결과를 여기에 반영
    for r in range(R):
        for c in range(C):
            if grid[r][c] <= 0: # 공기청정기나 빈 칸은 스킵하기 -> 확산할게 없으니까
                continue
            cnt = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != -1:
                    new_grid[nr][nc] += grid[r][c] // 5 # 4방향 확인해서 범위 안이고 청정기가 아닌 칸이며 먼지//5만큼 확산시키고 실제로 확산된 방향 수를 cnt에 누적한다.
                    cnt += 1
            new_grid[r][c] -= (grid[r][c] // 5) * cnt   # 확산된 만큼 현재 칸에서 빽. 4방향 모두 확산되었으면 dust//5*4를 뺀다!
    grid = new_grid # 결과가 담긴 new_grid를 grid로 교체하여 확산 완료된 상태로 두기

    # ② 위쪽 청정기 순환 (반시계)
    for i in range(top - 1, 0, -1):
        grid[i][0] = grid[i-1][0]
    for j in range(0, C - 1):
        grid[0][j] = grid[0][j+1]
    for i in range(0, top):
        grid[i][C-1] = grid[i+1][C-1]
    for j in range(C - 1, 1, -1):
        grid[top][j] = grid[top][j-1]
    grid[top][1] = 0

    # ③ 아래쪽 청정기 순환 (시계)
    for i in range(bot + 1, R - 1):
        grid[i][0] = grid[i+1][0]
    for j in range(0, C - 1):
        grid[R-1][j] = grid[R-1][j+1]
    for i in range(R - 1, bot, -1):
        grid[i][C-1] = grid[i-1][C-1]
    for j in range(C - 1, 1, -1):
        grid[bot][j] = grid[bot][j-1]
    grid[bot][1] = 0

    return grid

for _ in range(T):
    room = solve(room)

print(sum(sum(row) for row in room) + 2)