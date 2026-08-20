# 투 포인터를 사용해서 구간이 넓히면 합이 커지고, 좁히면 합이 작아지는 성질을 이용한다.
def solution(n):
    answer = 0
    left = 1
    right = 1
    total = 1
    
    while left <= n:    # left가 n보다 크다면 남은 구간으로 아무리 조합해도 n을 만들 수 없기에 n 이하까지 반복
        if total == n:  # 정답 찾았을 경우
            answer += 1
            total -= left   # 왼쪽 끝을 하나 빼고 포인터를 한 칸 옮긴다.
            left += 1   # 이렇게 하는 이유는 n을 표현하는 방법의 개수를 전부 세야하기 때문에 다른 시작점에 시작하는 또 다른 표현법을 찾아야한다.
        elif total < n: # 합이 부족할 때는 목표보다 작기 때문에 구간을 오른쪽으로 넓혀서 더 큰 수를 포함시킨다.
            right += 1
            total += right
        else:   # 합이 더 크면 구간을 왼쪽에서 좁혀서 작은 수를 뺀다.
            total -= left
            left += 1
    return answer