from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 시작점, 레버, 출구 위치 찾기
    start = None
    lever = None
    end = None
    
    for r in range(n):
        for c in range(m):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                end = (r, c)
    
    # BFS
    def BFS(start_pos, target):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[False] * m for _ in range(n)]
        q = deque()
        q.append((start_pos[0], start_pos[1], 0))   # (x, y, 거리)
        visited[start_pos[0]][start_pos[1]] = True
        
        while q:
            x, y, dis = q.popleft()
            # 목표 지점 도착
            if maps[x][y] == target:
                return dis
            
            # 델타탐색
            for r in range(4):
                nx = x + dx[r]
                ny = y + dy[r]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, dis + 1))
                        
        return -1
    # 1단계: S -> L(시작점에서 레버까지)
    dis1 = BFS(start, 'L')
    if dis1 == -1:
        return -1
    
    # 2단계: L -> E(레버에서 출구까지)
    dis2 = BFS(lever, 'E')
    if dis2 == -1:
        return -1
    
    return dis1 + dis2