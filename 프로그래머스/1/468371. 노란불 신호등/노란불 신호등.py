import math

def solution(signals):
    n = len(signals)
    
    # 모든 신호등 주기의 최소공배수 구하기
    periods = [G + Y + R for G, Y, R in signals]    # 각각의 시그널의 시간을 더한 값. 그래야지만 최소공배수를 구할 수 있다.
    res = periods[0]
    for i in periods[1:]:
        res = math.lcm(res, i)  # 최소공배수를 업데이트하면서 전체 순회 완료
        
    # 1초부터 res초까지 매초 확인을 할건데 이 res초 범위 안에서 답을 찾지 못하면 답이 없다고 보면 된다.
    for t in range(1, res + 1):
        all_yellow = True   # 지금 t초에서 모든 신호등이 노랑인지에 대한 flag
        for i, (G, Y, R) in enumerate(signals): # 각 신호등이 t초에 무슨 색인지 판별
            # t초일 때 이 신호등이 주기 내 몇 번째 초인가?
            pos = (t - 1) % periods[i]
            if not (G <= pos < G + Y):  # 노랑 구간이 아니라면
                all_yellow = False
                break
        if all_yellow:
            return t
        
    return -1