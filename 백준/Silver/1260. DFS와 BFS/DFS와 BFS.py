from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')

        for next_v in graph[v]:
            if not visited[next_v]:
                q.append(next_v)
                visited[next_v] = True

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬 -> 작은 번호부터! -> 정점 번호가 작은 것을 먼저 방문하기 위해 필요한 코드이다. 만약 정렬을 하지 않으면 입력 순서대로 리스트가 담기기 때문에 dfs에서 출력이 제대로 되지 않는다.
for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
dfs(V)
print()

visited = [False] * (N + 1) # 초기화
bfs(V)
