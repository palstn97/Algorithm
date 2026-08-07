def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    
    for i in range(0, len(score), m):
        if i + m <= len(score):
            box = []
            for j in range(i, i + m):
                box.append(score[j])
            answer += box[-1] * m
        
    return answer