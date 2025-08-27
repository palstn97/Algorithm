N = int(input())
mat = [list(map(float, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    x1, y1 = mat[i]
    x2, y2 = mat[(i + 1) % N]
    ans += x1 * y2 - x2 * y1

ans2 = abs(ans) / 2

print(round(ans2, 1))