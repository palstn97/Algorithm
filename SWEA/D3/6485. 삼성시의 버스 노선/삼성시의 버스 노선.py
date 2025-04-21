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


# 조금 더 좋은 풀이 -> 시간 단축 가능!
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus_list = [0]*5001
    for i in range(N):
        Ai, Bi = map(int, input().split())
        for stop in range(Ai, Bi + 1):
            bus_list[stop] += 1
    P = int(input())
    count = []
    for j in range(P):
        Cj = int(input())
        count.append(bus_list[Cj])

    print(f"#{tc} {' '.join(map(str, count))}")
