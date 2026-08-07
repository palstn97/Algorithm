def solution(number, limit, power):
    cnt = [0] * (number + 1)    # 약수의 갯수를 담아줄 리스트
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):   # 이렇게 하면 약수의 갯수가 올라간다.
            cnt[j] += 1
            
    answer = 0
    for i in range(1, number + 1):
        if cnt[i] <= limit:
            answer += cnt[i]
        else:
            answer += power
            
    return answer