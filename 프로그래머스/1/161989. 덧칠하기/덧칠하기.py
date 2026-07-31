def solution(n, m, section):
    # 시작 범위 설정하고 끝 범위 설정한 후 만약 section의 원소가 끝 범위보다 크다면 칠하는 횟수 1 증가시키고 범위 다시 설정하기
    answer = 1
    paint_start = section[0]
    paint_end = paint_start + m - 1
    
    for i in section[1:]:
        if i > paint_end:
            answer += 1
            paint_start = i
            paint_end = i + m - 1
    return answer