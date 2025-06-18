def solution(gems):
    answer = []
    short = len(gems) + 1

    l, r = 0, 0
    jewel = len(set(gems))  # 보석 종류 수
    jewel_cnt = 0           # 현재 윈도우 안의 보석 종류 수

    dic = {}

    while r < len(gems):
        gem = gems[r]
        if gem not in dic or dic[gem] == 0:
            dic[gem] = 1
            jewel_cnt += 1
        else:
            dic[gem] += 1
        r += 1

        while jewel_cnt == jewel:
            if r - l < short:
                short = r - l
                answer = [l + 1, r]

            dic[gems[l]] -= 1
            if dic[gems[l]] == 0:
                jewel_cnt -= 1
                l += 1
                break
            l += 1

    return answer
