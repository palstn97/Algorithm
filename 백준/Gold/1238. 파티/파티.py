import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())

# 단방향이어서 그래프가 두 개 필요하다!
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A].append((B, T))
    reverse_graph[B].append((A, T))

INF = int(1e9)  # 매우 큰 수로 설정

def dijkstra(start, graph): # 인자는 시작점과 그래프로 설정
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = [(0, start)] # (거리, 노드)

    while heap:
        dist, now = heapq.heappop(heap)

        # 이미 처리된 노드라면 넘어가기
        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:  # 인접 노드 확인하기
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return distance

# X에서 출발해서 모든 마을로 가는 최단 거리
back = dijkstra(X, graph)
# X에서 출발하고 역방향 그래프에서 모든 마을로 가는 최단거리인데...간선을 뒤집어서 설정을 했기 때문에 각 마을에서 출발해서 X까지 가는 최단거리이다!
go = dijkstra(X, reverse_graph)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, go[i] + back[i])

print(ans)