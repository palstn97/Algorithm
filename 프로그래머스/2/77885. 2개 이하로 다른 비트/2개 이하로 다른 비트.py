def solution(numbers):
    answer = []
    for n in numbers:
        num = n
        cnt = 0
        while n % 2 == 1:
            cnt += 1
            n //= 2
        answer.append(num + 2 ** (cnt - 1) if cnt != 0 else num + 1)
    return answer