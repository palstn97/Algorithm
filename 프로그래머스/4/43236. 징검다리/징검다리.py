def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()

    l, r = 0, rocks[-1]
    answer = 0

    while l <= r:   # l이 r보다 커지면 탐색 종료
        m = (l + r) // 2    # 정답의 후보로 중간값 설정하기 -> 이분탐색이니까
        del_rock = 0    # 제거할 바위 개수
        curr = 0    # 현재 바위 위치
        for rock in rocks:
            if rock - curr < m: # 탐색할 바위에서 현재 위치 뺀 값(거리)이 m보다 작다면 -> 바위 제거 -> 설정한 m보다 작기 때문에 간격 확보 불가
                del_rock += 1
            else:
                curr = rock # 현재 위치 갱신

        if del_rock <= n:   # 만약에 제거한 바위가 n보다 작거나 같으면
            answer = m  # 그게 답!
            l = m + 1   # 그래도 혹시 모르니 또 확인해야하니까 범위를 늘려서 확인
        else:
            r = m - 1   # 바위가 너무 많이 제거되었다면 m이 너무 크다는거니까 r을 줄여주기

    return answer