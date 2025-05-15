T = int(input())

for tc in range(1, T + 1):
    N, D = map(int, input().split())
    cnt = 0
    while N > (2 * D + 1) * cnt:
        cnt += 1

    print(f"#{tc} {cnt}")