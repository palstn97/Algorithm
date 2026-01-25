'''
브루트포스 사용해보기
기울기는 어떻게 생각???
두 지붕을 잇는 선분..? => 선분이 지나간다라는 것을 판단해보기
즉 오른쪽으로 가면서 기울기가 계속 증가하면 중간 건물들을 확인할 필요가 없다.
선분의 가파른 정도가 중요하고 그 가파른 정도는 기울기이다.
왼쪽에서 볼 때는 매우 큰 값으로 초기화하고 왼쪽으로 하나씩 확인하기
만약에 기울기가 감소하면 카운팅을 하나 추가
오른쪽에서 볼 때는 매우 작은 값으로 초기화하고 오른쪽으로 하나씩 확인하기
기울기가 계속 증가하면 카운팅을 하나 추가
'''
import sys
input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))

result = 0

# 각 건물을 기준으로
for i in range(N):
    cnt = 0
    # 왼쪽 확인하기
    min_slope = float('inf')
    for j in range(i - 1, -1, -1):
        slope = (buildings[j] - buildings[i]) / (j - i)
        if slope < min_slope:
            cnt += 1
            min_slope = slope

    # 오른쪽 확인하기
    max_slope = float('-inf')
    for j in range(i + 1, N):
        slope = (buildings[j] - buildings[i]) / (j - i)
        if slope > max_slope:
            cnt += 1
            max_slope = slope

    result = max(cnt, result)

print(result)