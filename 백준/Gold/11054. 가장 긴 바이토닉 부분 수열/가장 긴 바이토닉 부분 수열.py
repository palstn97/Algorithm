import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 바이토닉 수열은 어떤 지점을 기준으로 왼쪽은 증가하고 오른쪽은 감소하는 것이다.
# 그래서 각 인덱스 i에 대해 LTS[i]는 인덱스 i에서 끝나느 최장 증가 부분 수열 길이
# LDS[i]는 인덱스 i에서 시작하는 최장 감소 부분 수열 길이이다.
# 즉, i가 꼭짓점일 때 바이토닉 길이는 LIS[i] + LDS[i] - 1이 된다. 왜냐면 i를 두 번 세니까 1을 빼야한다.

# 왼쪽에서 오른쪽으로 LIS
lis = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            lis[i] = max(lis[i], lis[j] + 1)

# 오른쪽에서 왼쪽으로 lis(즉, 오른쪽 방향 lds)
lds = [1] * N
for i in range(N - 2, -1, -1):
    for j in range(i + 1, N):
        if A[j] < A[i]:
            lds[i] = max(lds[i], lds[j] + 1)

print(max(lis[i] + lds[i] - 1 for i in range(N)))