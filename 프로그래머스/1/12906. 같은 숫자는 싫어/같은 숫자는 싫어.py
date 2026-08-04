from collections import deque

def solution(arr):
    q = deque(arr)
    answer = []
    
    while q:
        now = q.popleft()
        if now not in answer or now != answer[-1]:
            answer.append(now)

    return answer