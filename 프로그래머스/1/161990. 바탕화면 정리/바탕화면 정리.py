def solution(wallpaper):
    min_raw, min_col = 50, 50
    max_raw, max_col = 0, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                min_raw = min(min_raw, i)
                min_col = min(min_col, j)
                max_raw = max(max_raw, i)
                max_col = max(max_col, j)
                
    answer = [min_raw, min_col, max_raw + 1, max_col + 1]   # 오른쪽 아래는 각각을 +1을 해야한다.
    return answer