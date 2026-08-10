from collections import deque

def solution(N, stages):
    fail = []
    
    stages.sort()
    q = deque(stages)
    
    for stage in range(1, N + 1):
        a = len(q)
        if a == 0:
            fail.append((stage, 0))
            continue
            
        b = 0
        while q and q[0] == stage:
            b += 1
            q.popleft()
            
        rate = b / a
        fail.append((stage, rate))
        
    # fail 리스트를 rate에 맞게 정렬을 해줄건데, 여기에서는 lambda 함수를 사용하기
    fail.sort(key = lambda x: x[1], reverse = True) # 실패율이 높은 스테이지부터 내림차순 -> reverse = True
    
    answer = []
    for i in range(len(fail)):
        answer.append(fail[i][0])
    
    return answer