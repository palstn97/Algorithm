import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, end = map(int, input().split())

# 다익스트라 활용하는 문제니까 heapq랑 distance 활용해보자. distance에는 각 노드까지의 최소 비용을 저장한다.
# 우선 distance 배열 초기화부터
distance = [float('inf')] * (N + 1)
distance[start] = 0 # 시작점은 일단 0

heap = []
heapq.heappush(heap, (0, start))

while heap:
    current_cost, current_node = heapq.heappop(heap)    # heap에서 가장 비용이 적은 (비용, 노드)를 꺼낸다. -> 확정되지 않은 노드 중 가장 가까운 노드부터 처리(최소 비용 꺼낸다.)

    if current_cost > distance[current_node]:   # 최적의 거리를 찾았다면 넘어가기(처리된 노드라면)
        continue
    if current_node == end:
        break

    for next_node, next_cost in graph[current_node]:    # 현재 노드에서 갈 수 있는 모든 이웃 확인
        new_cost = current_cost + next_cost # 새 경로의 총 비용 다시 설정
        if new_cost < distance[next_node]:  # 새로 발견한 경로가 기존보다 더 짧으면 업데이트하기
            distance[next_node] = new_cost
            heapq.heappush(heap, (new_cost, next_node)) # 업데이트된 노드를 heap에 추가

print(distance[end])