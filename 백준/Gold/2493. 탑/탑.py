N = int(input())
tower = list(map(int, input().split()))
hit = [0] * N

stack = []

for i in range(N):
    while stack:
        if tower[i] > tower[stack[-1]]:
            stack.pop()
        else:
            hit[i] = stack[-1] + 1
            break
    stack.append(i)

print(*hit)
