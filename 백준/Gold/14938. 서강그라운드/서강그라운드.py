import sys
input = sys.stdin.readline

def ground():
    n, m, r = map(int, input().split())
    items = [0] + list(map(int, input().split()))   # 입력이 1번부터 시작하기 때문에 0을 앞에 붙여준다.

    INF = float('inf')
    # dist[i][j] = i에서 j까지 최단거리
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신까지의 거리는 0
    for i in range(n + 1):
        dist[i][i] = 0

    for _ in range(r):
        a, b, l = map(int, input().split())
        # 같은 구간에 여러 도로가 있을 수 있으니 min으로 갱신
        dist[a][b] = min(dist[a][b], l)
        dist[b][a] = min(dist[b][a], l)

    # 플로이드-워셜: k를 경유지로 삼아서 모든 쌍 최단거리 갱신 -> 즉 k를 거쳐서 가는 게 더 짧으면 갱신하기! 경유지를 하나씩 늘려가면서 갱신하기. 최종적으로는 모든 노드를 자유롭게 경유한 최단거리가 완성
    for k in range(1, n + 1):   # k는 경유 노드
        for i in range(1, n + 1):   # i는 출발 노드
            for j in range(1, n + 1):   # j는 도착 노드
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    answer = 0

    # 각 노드를 출발점으로 수색 범위 m 이하 아이템 합산
    for start in range(1, n + 1):
        total = sum(items[i] for i in range(1, n + 1) if dist[start][i] <= m)
        answer = max(answer, total)

    print(answer)
# 입력 -> dist 배열 초기화 -> 간선 정보로 직접 연결된 노드들 거리 입력 -> 플로이드-워셜로 모든 쌍 최단거리 계산 -> 각 노드를 출발점으로 m 이하 거리 아이템 합산 -> 최댓값 출력
ground()
