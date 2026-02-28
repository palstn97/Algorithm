from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 델타 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 바이러스와 빈 칸을 저장해줄 리스트
virus = []
empty = []

for r in range(N):
    for c in range(M):
        if lab[r][c] == 2:
            virus.append((r, c))
        elif lab[r][c] == 0:
            empty.append((r, c))

def bfs(mat):
    q = deque(virus)    # 바이러스 위치에서 시작하기

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and mat[nr][nc] == 0:
                mat[nr][nc] = 2 # 감염!
                q.append((nr, nc))

ans = 0 # 전체 안전한 칸의 수
# 빈칸들 중에서 3개를 고르는(즉, 벽 3개 고르기!)
for i in combinations(empty, 3):
    # 각 조합마다 다 다르니까 lab을 복사해서 각각을 체크해야한다.
    tmp = [row[:] for row in lab]

    for r, c in i:
        tmp[r][c] = 1
    bfs(tmp)
    res = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                res += 1

    ans = max(ans, res)

print(ans)