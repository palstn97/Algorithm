from collections import deque

def solution(arr):
    q = deque(arr)
    answer = []
    
    while q:
        now = q.popleft()
        if now not in answer or now != answer[-1]:  # 뒤에 answer에 담겨있는게 또 나올 수도 있기 때문에 가장 마지막 원소를 비교했을 때 다르다면 추가하는 방식으로 진행하면 된다.
            answer.append(now)

    return answer