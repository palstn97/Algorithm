'''
다익스트라로 풉시다.
왜??
단일 시작점 최단 경로 문제이고 가중치가 양수인 간선들이다.
그리고 시작 정점에서 모든 다른 정점까지의 최단 거리를 구하는 것이기 때문!
우선순위 큐(힙)가 필수다.
리스트로 매번 최소값을 찾으면 시간 초과가 되기 때문이다.
중복 방문을 체크해야 한다.
그래프를 입력하는데 방향 그래프니까 이전의 그래프와는 달리 단방향으로만 저장해야한다.
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())    # 시작 정점

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)  # 최단 거리 계산해줄 리스트

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # 도착지, 가중치

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # (거리, 노드)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드라면 무시하기
        if distance[now] < dist:
            continue
        
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])