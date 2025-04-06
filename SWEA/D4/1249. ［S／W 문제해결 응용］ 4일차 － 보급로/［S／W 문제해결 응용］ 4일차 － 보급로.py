import heapq


def supply(start_r, start_c):
    INF = float('inf')
    distance = [[INF] * N for _ in range(N)]
    distance[start_r][start_c] = 0
    pq = [(0, start_r, start_c)]

    while pq:
        curr_weight, curr_r, curr_c = heapq.heappop(pq)

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(4):
            next_r = curr_r + dir[i][0]
            next_c = curr_c + dir[i][1]
            if 0 <= next_r < N and 0 <= next_c < N:
                new_weight = curr_weight + supply_matrix[next_r][next_c]
                if distance[next_r][next_c] > new_weight:
                    distance[next_r][next_c] = new_weight
                    heapq.heappush(pq, (new_weight, next_r, next_c))

    return distance[N - 1][N - 1]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    supply_matrix = [list(map(int, input())) for _ in range(N)]
    print(f"#{tc} {supply(0, 0)}")