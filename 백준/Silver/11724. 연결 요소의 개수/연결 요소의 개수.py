from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])  # 시작 노드를 큐에 넣기
    visited[start] = True   # 방문 처리

    while queue:    # 큐가 빌 때까지 반복하기
        node = queue.popleft()    # 맨 앞 노드 가져오기

        for next_node in graph[node]:
            if not visited[next_node]:  # 방문 안했으면?
                visited[next_node] = True   # 방문 처리하고
                queue.append(next_node) # 큐에 추가해주기

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 그래프 초기화(인접 리스트)

# 간선 정보 입력하기!
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향으로 연결되어 있으니까 두 번 append

visited = [False] * (N + 1)

cnt = 0
for i in range(1, N + 1):
    if not visited[i]:   # 아직 방문 안한 노드라면
        bfs(i)  # bfs 실행하기
        cnt += 1

print(cnt)
