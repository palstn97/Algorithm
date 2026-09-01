def solution(n):
    num = "124"
    answer = ''
    
    while n > 0:
        n -= 1
        r = n % 3
        answer = num[r] + answer
        n //= 3
    return answer