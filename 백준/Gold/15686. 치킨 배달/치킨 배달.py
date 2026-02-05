'''
조합을 사용해보기. 전체 치킨집 중에서 M개를 선택하는 문제니까 선택한ㄴ 치킨집들로 도시의 치킨 거리를 계산한다.
모든 선택 경우의 수를 다 확인해서 최소값을 찾을 것이다.
'''
from itertools import combinations

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 치킨집이랑 집을 분리해서 담을 리스트 생성
houses = []
chickens = []

# 집과 치킨집 위치를 우선 저장을 해야겠지? 단 행과 열 형태로 (r, c) 이런 형식으로 저장을 할 것이다.
for r in range(N):
    for c in range(N):
        if grid[r][c] == 1:
            houses.append((r, c))
        elif grid[r][c] == 2:
            chickens.append((r, c))

ans = float('inf')

# M개의 치킨집 조합을 선택을 해서 전체를 탐색을 할거다.
for chicken in combinations(chickens, M):
    distance = 0

    # 각 집마다 가장 가까운 치킨집까지의 거리를 계산
    for r, c in houses:
        min_distance = float('inf')
        for i, j in chicken:
            dis = abs(r - i) + abs(c - j)
            min_distance = min(min_distance, dis)
        distance += min_distance

    ans = min(ans, distance)

print(ans)