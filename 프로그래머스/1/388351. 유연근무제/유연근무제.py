def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        dead_line = (schedules[i] // 100) * 60 + (schedules[i] % 100) + 10
        res = 0
        for j in range(len(timelogs[i])):
            if (j + startday) % 7 == 6 or (j + startday) % 7 == 0:
                continue
            else:
                # 만약 9시 58분이면 10시 08분까지 와야하는데 그 부분을 처리해주어야 한다.
                real_time = (timelogs[i][j] // 100) * 60 + (timelogs[i][j] % 100)
                if real_time <= dead_line:
                    res += 1
        if res == 5:
            answer += 1
            
    return answer