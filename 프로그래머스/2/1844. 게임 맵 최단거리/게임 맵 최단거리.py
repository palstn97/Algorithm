from collections import deque

def solution(maps):
    n = len(maps)   # 행의 개수
    m = len(maps[0])    # 열의 개수
    
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    while q:
        curr_r, curr_c = q.popleft()
        for i in range(4):
            next_r = curr_r + dir[i][0]
            next_c = curr_c + dir[i][1]
            if 0 <= next_r < n and 0 <= next_c < m and visited[next_r][next_c] == 0:
                if maps[next_r][next_c] == 1:
                    maps[next_r][next_c] += maps[curr_r][curr_c]
                    q.append((next_r, next_c))
                visited[next_r][next_c] = 1 # 방문처리
                
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
