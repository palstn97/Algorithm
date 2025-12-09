from collections import deque

N = int(input())
lst = deque()
for i in range(1, N + 1):
    lst.append(i)

while len(lst) != 1:
    for j in range(N - 1):
        lst.remove(lst[0])
        first = lst.popleft()
        lst.append(first)

print(*lst)