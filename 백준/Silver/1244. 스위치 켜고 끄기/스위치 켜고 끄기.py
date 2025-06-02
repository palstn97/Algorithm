N = int(input())
arr = list(map(int, input().split()))
P = int(input())
for i in range(P):
    S, M = map(int, input().split())
    if S == 1:
        for j in range(1, N + 1):
            if 0 <= M * j - 1 < N:
                arr[M * j - 1] = 1 - arr[M * j - 1]
    else:
        arr[M - 1] = 1 - arr[M - 1]
        for k in range(1, N):
            if 0 <= M - 1 - k < N and 0 <= M - 1 + k < N:
                if arr[M - 1 - k] == arr[M - 1 + k]:
                    arr[M - 1 - k], arr[M - 1 + k] = 1 - arr[M - 1 - k], 1 - arr[M - 1 - k]
                else:
                    break

for i in range(0, N, 20):
    print(' '.join(map(str, arr[i:i + 20])))