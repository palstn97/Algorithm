'''
플로이드 워셜로 풀어볼 계획
모든 정점 쌍 사이의 최단 거리를 구하는 알고리즘이다.
다익스트라: 한 정점에서 다른 모든 정점까지
플로이드-워셜: 모든 정점에서 모든 정점까지
n이 작고, 간선이 많으면 플로이드-워셜을 사용하고
n이 크고, 간선이 적으면 다익스트라를 n번 사용해서 풀면된다!

핵심 아이디어는 "k를 거쳐가는 게 더 빠르면 갱신을 한다."
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 거리 테이블 초기화하기
dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0이다.
for i in range(1, n + 1):
    dist[i][i] = 0

# 간선 정보 입력하기!
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c) # 중복 노선 중 최소값 -> 같은 경로에 여러 버스가 있을 수 있으니 최소값만 저장을 하자!

# 여기서부터 플로이드-워셜 -> k를 먼저 돌려야만 거쳐가는 숫자가 점점 순차적으로 누적된다.
for k in range(1, n + 1):    # 경유지
    for i in range(1, n + 1):   # 출발지
        for j in range(1, n + 1):   # 도착지
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print() # 다음 줄로 넘어가기