def solution(x, n):
    answer = [x]
    k = x
    
    for i in range(1, n):
        x += k
        answer.append(x)
    return answer