from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)  # 양방향 연결
    graph[y].append(x)

def bfs(start):
    q = deque([start])
    visited = [False] * (N + 1)
    parent = [0] * (N + 1)  # 각 노드의 부모를 저장하기
    visited[start] = True   # 방문처리

    while q:
        v = q.popleft()

        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                parent[next_v] = v  # 부모에 현재 노드 기록
                q.append(next_v)

    return parent

parents = bfs(1)

for i in range(2, N + 1):
    print(parents[i])