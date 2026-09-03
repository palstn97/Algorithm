def solution(places):
    answer = []
    
    for place in places:
        grid = place
        violated = False    # 위반 여부
        # 모든 p의 좌표를 찾기
        seats = []
        for i in range(5):
            for j in range(5):
                if grid[i][j] == 'P':
                    seats.append((i, j))
                    
        for a in range(len(seats)):
            for b in range(a+1, len(seats)):
                x1, y1 = seats[a][0], seats[a][1]
                x2, y2 = seats[b][0], seats[b][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                
                if dist == 1:
                    violated = True
                elif dist == 2:
                    if x1 == x2 or y1 == y2:
                        mid_x = (x1+x2) // 2
                        mid_y = (y1+y2) // 2
                        if grid[mid_x][mid_y] != 'X':   # 파티션이 없다면
                            violated = True
                    else:
                        path1_blocked = grid[x1][y2]
                        path2_blocked = grid[x2][y1]
                        if path1_blocked != 'X' or path2_blocked != 'X':
                            violated = True
                                
        answer.append(0 if violated else 1)
        
    return answer