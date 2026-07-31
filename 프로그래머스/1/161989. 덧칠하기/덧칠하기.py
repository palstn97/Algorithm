def solution(n, m, section):
    answer = 1
    paint_start = section[0]
    paint_end = paint_start + m - 1
    
    for i in section[1:]:
        if i > paint_end:
            answer += 1
            paint_start = i
            paint_end = i + m - 1
    return answer