# 어짜피 가장 큰 수를 만드는거니까 숫자의 갯수가 중요하고 그 갯수를 센 다음에 둘 중 작은것을 선택을 해주면 된다.
# 둘 중 작은것을 answer에 담아주고 이때, 9에서부터 탐색을 하면서 담아주면 큰 수가 될 것이다.
# 예외처리도 반드시 해주기!

def solution(X, Y):
    cnt_x = [0] * 10
    cnt_y = [0] * 10
    answer = ''
    
    for i in X:
        cnt_x[int(i)] += 1
    for j in Y:
        cnt_y[int(j)] += 1
        
    for k in range(9, -1, -1):
        common = min(cnt_x[k], cnt_y[k])
        answer += str(k) * common
        
    # 예외 처리
    if not answer:
        return '-1'
    if answer == '0' * len(answer):
        return '0'
    
    return answer