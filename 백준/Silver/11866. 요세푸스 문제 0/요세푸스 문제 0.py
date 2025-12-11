from collections import deque

N, K = map(int, input().split())
q = deque()
result = []

for i in range(1, N + 1):
    q.append(i)

while q:
    # 맨 앞을 맨 뒤로 보내기 -> K - 1번 회전을 하면 K 번째 사람이 리스트의 가장 앞으로 온다.
    for _ in range(K - 1):
        q.append(q.popleft())
    
    # k번째 사람 제거하고 result에 담아주기
    result.append(q.popleft())

# join은 str
print('<' + ', '.join(map(str, result)) + '>')