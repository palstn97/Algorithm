T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        for r in range(1, j + 1):
            if 0 <= i - 1 - r and i - 1 + r < N:
                if arr[i - 1 - r] == arr[i - 1 + r]:
                    arr[i - 1 - r] = arr[i - 1 + r] = 1 - arr[i - 1 - r]

    print(f"#{tc} {' '.join(map(str, arr))}")