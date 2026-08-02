def solution(video_len, pos, op_start, op_end, commands):
    video_len = int(video_len[:2]) * 60 + int(video_len[3:])
    pos = int(pos[:2]) * 60 + int(pos[3:])
    op_start = int(op_start[:2]) * 60 + int(op_start[3:])
    op_end = int(op_end[:2]) * 60 + int(op_end[3:])
    
    if op_start <= pos <= op_end:
        pos = op_end
    
    for command in commands:
        if command == "prev":
            if pos < 10:
                pos = 0
            else:
                pos = pos - 10
        elif command == "next":
            if video_len - pos < 10:
                pos = video_len
            else:
                pos = pos + 10
        # 만약 또 오프닝 시간 사이에 있으면 오프닝 끝나는 시간으로 돌리는 것을 매번 확인해주어야 한다.
        if op_start <= pos <= op_end:
            pos = op_end
    
    # 변환하기 -> f"{변수:포맷스팩}" -> :뒤에 오는 포맷스팩은 숫자를 어떻게 표시할지이다. -> str 형태이다. 포맷팅된 문자열을 만드는 문법이 f-string기법이다. 잘 외워둘 것!
    # 02d는 정수로 표시하는데 2는 최소 자릿수를 2자리로 맞추고 자릿수가 모자라면 0으로 채운다는 뜻이다.
    minutes = pos // 60
    seconds = pos % 60
    answer = f"{minutes:02d}:{seconds:02d}"
        
    return answer