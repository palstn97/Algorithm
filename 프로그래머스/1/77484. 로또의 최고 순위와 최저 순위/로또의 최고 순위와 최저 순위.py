def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)  # 0의 개수 세기
    num = 0
    
    for i in lottos:
        if i in win_nums:
            num += 1
    
    min_rank = 7 - num
    max_rank = 7 - (num + zero_cnt)
    
    if min_rank >= 6:
        min_rank = 6
    if max_rank >= 6:
        max_rank = 6
    answer = [max_rank, min_rank]
    return answer