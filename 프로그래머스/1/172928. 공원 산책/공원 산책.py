def solution(park, routes):
    n = len(park)
    m = len(park[0])
    
    move = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    # 시작 위치 찾기
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                r, c = i, j
                
    for route in routes:
        d, p = route.split()
        p = int(p)  # 처음에는 문자열이니까 정수형으로 변환 필요
        dr, dc = move[d]
        
        nr = r
        nc = c
        
        for i in range(p):
            nr += dr
            nc += dc
            if not(0 <= nr < n and 0 <= nc < m) or park[nr][nc] == 'X':
                break
        else:
            r, c = nr, nc
                
    answer = [r, c]
    return answer