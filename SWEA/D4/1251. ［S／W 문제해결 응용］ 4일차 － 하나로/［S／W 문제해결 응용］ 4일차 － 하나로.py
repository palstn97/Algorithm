import heapq


def one_way(start):
    visited = [False] * N
    pq = [(0, start)]
    min_sum = 0

    while pq:
        weight, node = heapq.heappop(pq)
        if visited[node]:
            continue

        visited[node] = 1
        min_sum += weight

        for next_node in range(N):
            if visited[next_node] == 0:
                heapq.heappush(pq, (graph[node][next_node], next_node))

    return min_sum


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    X_lst = list(map(int, input().split()))
    Y_lst = list(map(int, input().split()))
    E = float(input())
    graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                graph[i][j] = (X_lst[i] - X_lst[j]) ** 2 + (Y_lst[i] - Y_lst[j]) ** 2
    min_cost = one_way(0)
    result = E * min_cost
    print(f"#{tc} {round(result)}")