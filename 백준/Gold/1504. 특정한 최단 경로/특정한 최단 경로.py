import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c)) # 양방향 정보 저장

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = [(0, start)] # (거리, 노드)

    while heap:
        dist, now = heapq.heappop(heap)

        # 이미 처리된 노드라면?
        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return distance

# 각 지점에서 출발하는 최단거리
dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

# 경로1: 1 -> v1 -> v2 -> N
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
# 경로2: 1 -> v2 -> v1 -> N
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

ans = min(path1, path2)

if ans >= INF:
    print(-1)
else:
    print(ans)