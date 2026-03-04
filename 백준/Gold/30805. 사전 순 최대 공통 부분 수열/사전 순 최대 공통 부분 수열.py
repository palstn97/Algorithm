'''
공통 부분 수열이란 두 수열에서 순서를 유지하면서 공통으로 뽑을 수 있는 수열
사전 순 비교는 앞자리부터 비교 시작
핵심 아이디어는 그래서 뭐냐? 그리디
왜? 앞자리가 클수록 유리하니까, 매 단계에서 남은 범위 내 공통 원소 중 최댓값을 고르면 된다.
'''
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

result = []
ia, ib = 0, 0   # 현재 탐색 시작 위치 -> 이미 선택한 원소 이전으로 돌아가지 못하게 하는 역할

while ia < N and ib < M:
    # 현재 범위에서 공통 원소 찾기
    common = set(A[ia:]) & set(B[ib:])
    if not common:  # 공통 원소가 없으면 종료하기
        break

    max_val = max(common)   # 공통 원소 중 최댓값

    # 각 수열에서 max_val의 위치 찾아서 포인터 업데이트하기!
    ia = A.index(max_val, ia) + 1   # ia부터 탐색해서 위치  + 1 -> .index(찾을값, 시작 위치) -> 그러면 리스트 A에서 ia번째부터 max_val을 찾기
    ib = B.index(max_val, ib) + 1   # ib번째부터 max_val을 찾아서, 그 위치 + 1을 새로운 ib로 하기!

    result.append(max_val)

print(len(result))
if result:
    print(*result)
else:
    print()