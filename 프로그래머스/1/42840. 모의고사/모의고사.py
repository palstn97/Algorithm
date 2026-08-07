# 패턴화시킨 후 정답과 비교를 해본다.

def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1, score2, score3 = 0, 0, 0
    
    for i, answer in enumerate(answers):
        if answer == pattern1[i % len(pattern1)]:
            score1 += 1
        if answer == pattern2[i % len(pattern2)]:
            score2 += 1
        if answer == pattern3[i % len(pattern3)]:
            score3 += 1
            
    scores = [score1, score2, score3]
    max_score = max(scores)
    result = []
    for i in range(3):
        if scores[i] == max_score:
            result.append((i + 1))
            
    return result