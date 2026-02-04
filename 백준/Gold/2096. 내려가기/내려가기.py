'''
처음에는 다익스트라를 생각했지만 다익스트라는 그래프에서 임의의 노드 간 최단 경로를 구할 때 사용이 되고
경로가 여러 방향으로 갈 수 있을 때 사용한다. 또한 어떤 노드를 먼저 방문해야 할지 우선순위가 필요한 문제에 사용된다.
하지만 이 문제는 위에서 아래로만 이동하는 방향이 하나인 경우이고 각 행을 순서대로 처리하면 된다.
이전 행의 결과만 알면 다음 행 계산이 가능하기 때문에
dp를 사용하는 문제이다.
'''
import sys
input = sys.stdin.readline

N = int(input())

# 첫 행 입력
first = list(map(int, input().split()))
# first를 복사해서 새로운 리스트를 만드는데 이 리스트는 각각 최대랑 최소를 구하는 데 필요하다. 각 위치에서의 최대 점수, 최소 점수를 저장하는 리스트!
max_dp = first[:]
min_dp = first[:]

# 나머지 행 처리
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    new_max = [a + max(max_dp[0], max_dp[1]), b + max(max_dp[0], max_dp[1], max_dp[2]), c + max(max_dp[1], max_dp[2])]
    new_min = [a + min(min_dp[0], min_dp[1]), b + min(min_dp[0], min_dp[1], min_dp[2]), c + min(min_dp[1], min_dp[2])]

    # 업데이트하기 -> 각각의 행까지의 최대 점수, 최소 점수
    max_dp = new_max
    min_dp = new_min

print(max(max_dp), min(min_dp))