T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    lst = []
    for _ in range(P):
        Cj = int(input())
        count = 0
        for i in range(N):
            bus = []
            for k in range(matrix[i][0], matrix[i][1] + 1):
                bus.append(k)
            if Cj in bus:
                count += 1
        lst.append(count)
    print(f"#{tc} {' '.join(map(str, lst))}")
