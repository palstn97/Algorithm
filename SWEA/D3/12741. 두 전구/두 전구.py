T = int(input())

for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    finish_time = min(B, D)
    start_time = max(A, C)
    result = finish_time - start_time
    if result > 0:
        print(f"#{tc} {result}")
    else:
        print(f"#{tc} {0}")