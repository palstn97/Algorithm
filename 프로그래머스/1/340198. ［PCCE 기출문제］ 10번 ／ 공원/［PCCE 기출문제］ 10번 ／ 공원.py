def solution(mats, park):
    n = len(park)
    m = len(park[0])
    mats.sort(reverse=True) # 큰거부터 확인해서 적합하면 끝낼 수 있도록 한다.
    
    for s in mats:
        for i in range(n):
            for j in range(m):
                if check(park, i, j, s, n, m):
                    return s
                
    return -1

def check(park, x, y, size, n, m):
    if x + size > n or y + size > m:
        return False
    for i in range(x, x + size):
        for j in range(y, y + size):
            if park[i][j] != "-1":  # 빈자리가 아니면 False 반환
                return False
            
    return True # 그 외에는 다 True 처리