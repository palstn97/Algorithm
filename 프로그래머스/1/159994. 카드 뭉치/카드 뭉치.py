# 순서를 맞추니까 선입선출을 생각하면 큐를 사용하는게 좋을것 같다.
# for문을 사용하여 goal 리스트를 순회하면 그 순서에 맞는지 확인하고 순서가 맞지 않다면 No를 반환하면 된다.

from collections import deque

def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    
    for i in goal:
        if q1 and q1[0] == i:   # q1이 존재하고 q1의 첫 번째 원소가 i랑 동일하면 q1을 빼주자.
            q1.popleft()
        elif q2 and q2[0] == i:
            q2.popleft()
        else:
            return 'No'
        
    return 'Yes'