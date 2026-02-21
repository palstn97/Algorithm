'''
일단은 그래프인데
웜홀이 등장하면서 웜홀의 이동 시간이 음수이다.
그러면 bfs나 다익스트라일까? 그건 아니지 bfs는 가중치가 있는 그래프에 부적합하고 다익스트라는 음수 간선이 있으면 동작을 안하니까.
그렇다면 벨만-포드이다. 음수 간선이 가능하니까 음수 사이클 감지가 가능하다.
핵심 아이디어로는 출발점으로 돌아왔을 때 시간이 줄어드는 경로(음수 사이클)가 존재하는가??
'''
import sys
input = sys.stdin.readline

def bellman_ford(n, edges):
    # 모든 노드를 시작점으로 설정(연결 안 된 컴포넌트도 탐지하기 위해서 0으로)
    dist = [0] * (n + 1)    # dist[i] = 시작점에서 노드 i까지 현재 알고 있는 최단거리 -> INF가 아닌 0인 이유는 최단거리를 구하는 것이 아닌 음수 사이클을 탐지하는 것이 목표이기 때문이다.
    # n-1번 반복
    for i in range(n):
        for u, v, w in edges:   # 모든 간선 확인하기
            # u를 거쳐서 v로 가는게 더 짧으면 갱신하기
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if i == n - 1:  # n번쩨 반복 -> 정상적인 그래프라면 n번째 반복에서 더 이상 갱신이 없어야 한다.
                    return True
    return False
# n-1번 동안 최단 거리를 계속 갱신을 하고 n-1번째 과정에서 최단거리가 확정된다. 만약 n번째에서 갱신이 발생하면 yes이고 갱신이 없다면 no(음수 사이클 없음)

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []

    # 도로: 양방향, 양수 가중치 -> 도로는 왔다갔다 할 수 있기 때문에 두 방향 모두 추가
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    # 웜홀: 단방향, 음수 가중치 (시간이 줄어드니까) -> 웜홀은 한 방향만이고 시간이 줄어드니까 -T로 추가하기
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    if bellman_ford(N, edges):
        print("YES")
    else:
        print("NO")