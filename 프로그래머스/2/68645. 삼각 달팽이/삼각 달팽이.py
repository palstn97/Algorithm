def solution(n):
    triangle = [[0] * (i + 1) for i in range(n)]
    x, y = -1, 0    # 초기 위치
    total = n * (n + 1) // 2    # 사각형에 들어가는 총 숫자의 갯수
    num = 0
    
    dr = [1, 0, -1] # 아래, 오른쪽, 위대각선
    dc = [0, 1, -1]
    i = 0
    
    for _ in range(total):
        x, y = x + dr[i], y + dc[i]
        num += 1
        triangle[x][y] = num
        
        nx = x + dr[i]
        ny = y + dc[i]
        # 다음 칸이 삼각형 범위를 벗어나거나 이미 채워졌으면 방향을 전환하기
        if nx < 0 or nx >= n or ny < 0 or ny > nx or triangle[nx][ny] != 0:
            i = (i + 1) % 3
            
    answer = []
    for r in range(n):
        for c in range(r + 1):
            answer.append(triangle[r][c])
    return answer