import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
truth_input = list(map(int, input().split()))
truth_count = truth_input[0]
truth_people = set(truth_input[1:])
# 이 방법도 가능 -> truth_people = set(truth_input[1:] if truth_count > 0 else set())

graph = [[] for _ in range(N + 1)]
parties = []

for _ in range(M):
    party_input = list(map(int, input().split()))
    party_size = party_input[0]
    party_members = party_input[1:]
    parties.append(party_members)

    # 같은 파티 사람들끼리 연결하기
    for i in range(party_size):
        for j in range(i + 1, party_size):
            graph[party_members[i]].append(party_members[j])
            graph[party_members[j]].append(party_members[i])

def bfs():
    q = deque(truth_people) # 진실을 아는 사람부터 큐에 넣어주기
    visited = [False] * (N + 1)
    # 진실 아는 사람들 방문 처리
    for p in truth_people:
        visited[p] = True

    while q:
        current = q.popleft()

        # 현재 사람과 연결된 모든 사람 확인하기 -> 서로 하나의 파티에 연결이 되어 있으면 진실이 전파된다.
        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True
                truth_people.add(next_node) # 진실을 아는 사람들 집단에 해당하는 사람을 담아준다.
                q.append(next_node)

    cnt = 0 # 거짓말이 가능한 파티를 셀거야
    for party in parties:
        if not any(person in truth_people for person in party): # 진실을 아는 사람이 파티에 하나라도 포함이 된다면 true
            cnt += 1
    return cnt

ans = bfs()
print(ans)