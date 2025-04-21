T = int(input())
matrix = [list(map(int, input().split())) for _ in range(T)]
grid = [[0] * 100 for _ in range(100)]
total = 0
for i in range(T):
    for r in range(matrix[i][0], 10 + matrix[i][0]):
        for c in range(matrix[i][1], 10 + matrix[i][1]):
            grid[r][c] += 1

for j in range(100):
    for k in range(100):
        if grid[j][k] != 0:
            total += 1

print(total)