def solution(storey):
    answer = 0
    carry = 0   # 이전 자리수에서 올라온 값
    
    while storey > 0:
        d = storey % 10 + carry # 현재 자릿수
        storey //= 10
        
        if d <= 4:
            answer += d
            carry = 0
        elif d == 5:
            if storey % 10 >= 5:    # 위의 자리가 5 이상이면
                answer += 5
                carry = 1   # 자리 올림이 되니까 carry를 1로
            else:
                answer += 5 # 여긴 굳이 자릿수를 올릴 필요 없으니까 -를 한다고 생각을 하면 carry는 0이 된다.
                carry = 0
        else:
            answer += (10 - d)
            carry = 1
            
    return answer + carry