T = int(input())

for tc in range(1, T + 1):
    a, b, c = list(map(int, input().split()))
    grid = [0] * 101
    result = 0

    if a == b == c:
        result = a

    grid[a] += 1
    grid[b] += 1
    grid[c] += 1

    for j in range(101):
        if grid[j] == 1:
            result = j
            break

    print(f"#{tc} {result}")