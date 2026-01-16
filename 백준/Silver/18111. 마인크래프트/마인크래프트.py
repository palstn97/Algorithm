'''
모든 경우를 다 해봐야지만 최적해를 찾을 수 있는 문제같다..?
그러면 그리디랑 브루트포스는 어떻게 비교할 것인가?
정렬하면 규칙이 보이는지? -> 이러면 그리디를 시도하자.
그게 아니라면 반례가 떠오르는지 생각하고 반례가 떠오르면 그리디는 사용할 수 없다.
범위가 작은지 판단!(N <= 500, K <= 1000 등) -> 브루트포스
크다면?
부분 문제가 반복되는지 확인해보자 -> 이 경우에는 DP를 사용할 것이다.
모르면 일단 무조건 브루트포스로 시작하자.
'''
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 시간 초과가 나는 이유는 다 높이를 다 돌아서... 그래서 grid 안에 있는 최소 높이랑, 최대 높이 사이에만 만들어줄거다.
min_height = min(min(row) for row in grid)
max_height = max(max(row) for row in grid)

min_time = float('inf')
height = 0

for h in range(min_height, max_height + 1):    # 이건 모든 최적의 높이 찾는거
    remove = 0  # 캐낸 블록
    add = 0 # 추가할 블록
    for i in range(N):  # grid 돌자
        for j in range(M):
            diff = grid[i][j] - h
            if diff > 0:    # 높이가 최적보다 더 높으니까 없애야지
                remove += diff
            else:
                add += abs(diff)
    if B + remove - add >= 0:
        time = remove * 2 + add
        if time <= min_time:
            min_time = time
            height = h

print(min_time, height)