def cargo(adj_matrix):
    # 끝나는 시간 기준으로 정렬
    adj_matrix.sort(key=lambda x: x[1])

    curr_start, curr_end = adj_matrix[0]
    truck_sum = 1  # 첫 작업 선택했다고 보고 시작

    for i in range(1, len(adj_matrix)):
        next_start, next_end = adj_matrix[i]
        if next_start >= curr_end:
            curr_start, curr_end = next_start, next_end
            truck_sum += 1

    return truck_sum


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    time_matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {cargo(time_matrix)}")