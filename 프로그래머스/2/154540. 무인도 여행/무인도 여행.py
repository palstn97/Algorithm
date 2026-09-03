from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    answer = []
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for r in range(n):
        for c in range(m):
            if maps[r][c] != 'X' and not visited[r][c]:
                # 새로운 섬을 발견했기에 bfs를 실행
                q = deque([(r, c)])
                visited[r][c] = True    # 방문처리
                total_sum = int(maps[r][c]) # 식량 총합
                
                while q:    # q에 뭐라도 있으면
                    x, y = q.popleft()  # 꺼내고...
                    for i in range(4):  # 4방향 탐색
                        nx = x + dr[i]
                        ny = y + dc[i]
                        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            total_sum += int(maps[nx][ny])
                            q.append((nx, ny))
                            
                answer.append(total_sum)
                
    if not answer:
        return [-1]
    return sorted(answer)