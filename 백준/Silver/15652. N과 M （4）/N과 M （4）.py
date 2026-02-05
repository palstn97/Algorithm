N, M = map(int, input().split())
result = [] # 현재 선택한 숫자들을 저장하는 리스트

def backtrack(start):   # start는 이번에 선택할 숫자의 시작점을 의미한다.
    # 종료 조건
    if len(result) == M:    # result에 M개가 모였는지 체크
        print(*result)
        return  # 해당 경로는 끝
    
    # 후보 탐색
    for i in range(start, N + 1):   # 비내림차순이기 때문에 이전보다 작은 숫자는 선택하지 않는다.
        result.append(i)
        backtrack(i)    # 재귀 호출: 다음 숫자를 선택하러 간다. i를 넘겨서 동일한 숫자도 뽑을 수 있도록 한다.
        result.pop()    # 재귀에서 돌아온 후 마지막 숫자를 제거한다. -> 백트래킹: 이전 상태로 돌아간다. 다른 선택을 시도하기 위해서!

backtrack(1)

'''
중복 조합 사용하는 방법
from itertools import combinations_with_replacement

N, M = map(int, input().split())

for comb in combinations_with_replacement(range(1, N+1), M):
    print(*comb)
'''