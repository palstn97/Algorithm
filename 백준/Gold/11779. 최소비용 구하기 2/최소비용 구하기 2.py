import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]  # 다익스트라는 인접 리스트 사용해서 그래프를 구성한다. graph[a]에 (도착도시, 비용)을 추가하기 -> n + 1인 이유는 도시 번호가 1번부터 시작이니까!
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

INF = float('inf')
dist = [INF] * (n + 1)  # dist[i]는 출발점에서 도시 i까지의 최단거리이다. 처음에는 무한대로 초기화
prev = [-1] * (n + 1)   # prev[i]는 도시 i에 오기 직전 도시. 경로 역추적에 사용하고 -1은 아직 아무도 안왔다는 것을 의미한다.
dist[start] = 0 # 출발점은 자기 자신까지 거리가 0이다

def solve():
    heap = [(0, start)] # (현재까지의 비용, 현재 도시) 형태의 최소힙. 출발점을 비용 0으로 힙에 넣고 시작
    while heap:
        cost, u = heapq.heappop(heap)   # 현재 비용이 가장 작은 노드를 꺼낸다.

        if cost > dist[u]:  # 이미 더 짧은 경로로 u를 처리했다면 넘어가기. 힙에 같은 노드가 여러 번 들어갈 수 있는데, 오래된 버전은 무시!
            continue

        for v, w in graph[u]:   # u의 모든 이웃 도시 v를 확인
            if dist[u] + w < dist[v]:   # u를 거쳐서 v로 가는 비용. 기존 dist[v]보다 더 싸면 갱신하기
                dist[v] = dist[u] + w
                prev[v] = u # v에 오기 직전이 u임을 기록하기 -> 경로 추적용
                heapq.heappush(heap, (dist[v], v))  # 갱신된 v를 힙에 추가해서 나중에 처리하기

solve()

# 경로 역추적
# 도착점 end부터 prev를 따라 거슬러 올라간다. prev[출발점] = -1이므로 출발점까지 올라가면 종료하기.
path = []
cur = end
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()

print(dist[end])
print(len(path))
print(*path)