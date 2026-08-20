def solution(board, h, w):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    check = board[h][w]
    answer = 0
    
    for i in range(4):
        nr = h + dr[i]
        nc = w + dc[i]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
            if board[nr][nc] == check:
                answer += 1

    return answer