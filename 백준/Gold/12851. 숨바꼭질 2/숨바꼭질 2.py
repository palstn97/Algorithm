from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# dist[i] = 위치 i에 도달하는 최단 시간 / cnt[i] = 위치 i에 최단 시간으로 도달하는 경우의 수
dist = [-1] * 100001    # visited를 대체한다. 미방문 표시 역할
cnt = [0] * 100001  # 경우의 수

# 초기값 설정
dist[N] = 0
cnt[N] = 1

q = deque()
q.append(N) # 수빈이 위치 담아주기

while q:
    curr = q.popleft()
    for next in [curr - 1, curr + 1, curr * 2]: # 현재 위치에서 이동 가능한 세 가지 이동 후보를 순서대로 탐색
        if next < 0 or next >= 100001:
            continue    # 범위를 벗어난다면 스킵하기
        if dist[next] == -1:    # 처음 방문하는 경우??? -> 이게 곧 최단거리.
            dist[next] = dist[curr] + 1 # 시간은 현재 + 1
            cnt[next] = cnt[curr]   # 경우의 수는 현재까지 온 경우의 수를 그대로 받는다.
            q.append(next)  # 다음 탐색
        elif dist[next] == dist[curr] + 1:  # 만약 같은 최단시간으로 다시 도달한다면? 큐에 추가는 이미 했기 때문에 cnt만 누적
            cnt[next] += cnt[curr]
# 더 빠른 경로가 이미 있는 경우는 위의 조건문에 걸리지 않기 때문에 알아서 무시된다.
print(dist[K])
print(cnt[K])