from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    lst = set()
    for l in range(1, len(numbers) + 1):
        for p in permutations(numbers, l):   # 각각의 갯수만큼 순열 뽑기
            lst.add(int(''.join(p)))    # 튜플을 문자열로 합친 뒤 정수로 변환하기 -> 정수로 변환하는 이유는 앞에 0이 붙는 경우에는 그 0을 뺀것과 동일한 값이기 때문에 정수로 변환하면 자동으로 변환이 된다.
    
    answer = 0
    for num in lst:
        if is_prime(num):
            answer += 1

    return answer