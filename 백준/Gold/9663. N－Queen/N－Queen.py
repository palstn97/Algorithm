'''
브루트포스??
그러기에는 너무 경우의 수가 많아진다. 왜냐면 각 칸마다 놓는다/안놓는다 2가지 선택지가 있으니까.
그래서 어떤걸 쓸까?
백트래킹을 사용해보자.
즉, 가지치기를 사용하는 것이다. 중간에 '이 방법은 안될 것 같다' 싶으면 즉시 중단하고 다른 경로를 탐색한다.
백트래킹의 핵심 3단계
1. 선택: 현재 단계에서 가능한 선택을 하기
2. 탐색: 그 선택이 유망한지 확인하고 유망하다면 다음 단계로 직행한다. 불가능하면 즉시 중단해서 가지치기 한다!
3. 취소: 탐색이 끝나면 선택을 취소하고 다른 선택을 시도한다.

백트래킹 템플릿은?
def backtrack(현재상태):
    # 종료 조건: 목표에 도달했나?
    if 목표_달성:
        결과_저장()
        return
    
    # 가능한 선택지들을 시도
    for 선택 in 가능한_선택들:
        # 1. 이 선택이 유망한가? (가지치기)
        if not 조건_만족(선택):
            continue  # 불가능하면 스킵!
        
        # 2. 선택하기
        선택_적용(선택)
        
        # 3. 다음 단계로
        backtrack(다음_상태)
        
        # 4. 선택 취소 (백트래킹)
        선택_취소(선택)
'''
N = int(input())
# 전역 변수로 선언
col_used = [False] * N
diag1_used = [False] * (2 * N - 1)
diag2_used = [False] * (2 * N - 1)

def backtrack(row):
    # 모든 행에 퀸을 다 놓았으면 성공
    if row == N:
        return 1
    cnt = 0
    # 이번 행의 각 열에 놓아보기
    for col in range(N):
        # 이 위치에 놓을 수 있는가?
        if col_used[col] or diag1_used[row - col + N - 1] or diag2_used[row + col]:
            continue    # 불가능하면 스킵

        # 퀸 놓기
        col_used[col] = True
        diag1_used[row - col + N - 1] = True
        diag2_used[row + col] = True

        # 다음 행으로 이동
        cnt += backtrack(row + 1)

        # 퀸 제거(백트래킹)
        col_used[col] = False
        diag1_used[row - col + N - 1] = False
        diag2_used[row + col] = False

    return cnt

print(backtrack(0))