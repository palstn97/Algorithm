from itertools import combinations

def solution(number):
    answer = 0
    for comb in combinations(number, 3):    # number라는 리스트에서 3명을 뽑는 조합! -> 조합 함수 알아두기
        if sum(comb) == 0:
            answer += 1
    return answer