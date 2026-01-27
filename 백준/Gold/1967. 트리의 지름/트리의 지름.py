'''
트리에서 가장 먼 두 노드 사이의 거리를 구하자. -> 모든 노드 쌍의 거리를 다 구해?
이렇면 시간이 터진다.
트리의 특성을 생각해보자.
트리는 사이클이 없고 두 노드 사이의 경로가 단 하나만 존재한다.
그러면 어디에서 시작하던지 첫 번재 bfs에서 찾은 노드는 항상 지름의 한 쪽 끝이라는 결론이 생긴다.
이러면 찾은 곳에서 다시 bfs를 시작하면 나머지 반대 쪽도 찾을 수 있다.
'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

# 트리를 인접 리스트로 저장하고 이때, 트리니까 양방향으로 저장할 것
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

# bfs 함수로 start에서 모든 노드까지의거리를 구한다.
def bfs(start):
    visited = [-1] * (n + 1)    # -1은 아직 방문하지 않았다.
    visited[start] = 0
    q = deque([start])

    max_dist = 0    # 최대 거리
    result_node = start   # 가장 먼 노드

    while q:
        now = q.popleft()

        # 현재 노드와 연결된 모든 노드 확인하기
        for next_node, weight in graph[now]:
            if visited[next_node] == -1:
                visited[next_node] = visited[now] + weight  # 거리 계산: 현재까지의 거리 + 간선 가중치
                q.append(next_node)

                # 최대 거리 갱신 작업
                if visited[next_node] > max_dist:
                    max_dist = visited[next_node]
                    result_node = next_node

    return result_node, max_dist

node1, _ = bfs(1)   # 임의의 노드에서 가장 먼 노드 찾기
node2, diameter = bfs(node1)

print(diameter)