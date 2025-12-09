N = int(input())
point = []

for i in range(N):
    xi, yi = map(int, input().split())
    point.append((xi, yi))

point.sort()

for x, y in point:
    print(x, y)