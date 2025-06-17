from collections import deque


def bfs(S):
    q = deque([S])
    visited = [0] * (N + 1)
    cnt = 0
    visited[S] = 1  # 방문처리하기

    while q:    # q가 빌때까지 반복
        V = q.popleft()
        cnt += 1
        for i in graph[V]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

    return cnt


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

max_cnt = 0
result = []

for j in range(1, N + 1):
    cnt = bfs(j)
    if cnt > max_cnt:
        max_cnt = cnt
        result = [j]
    elif cnt == max_cnt:
        result.append(j)

print(' '.join(map(str, result)))