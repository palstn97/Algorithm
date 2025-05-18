for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        arr.sort()
        arr[-1] -= 1
        arr[0] += 1

    arr.sort()
    print(f"#{tc} {arr[-1] - arr[0]}")
