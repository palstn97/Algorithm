N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N    # 어찌됐든 최소는 자기 자신을 포함하니까 1로 싹 다 초기화

for i in range(1, N):
    for j in range(i):  # i 앞에 있는 모든 원소 확인하기
        if arr[i] > arr[j]: # 증가 수열이라면
            dp[i] = max(dp[i], dp[j] + 1)   # dp 갱신하는데 현재 길이와 새로 계산한 길이 중에 더 긴 거 선택하기

print(max(dp))  # dp중 최댓값 구하기