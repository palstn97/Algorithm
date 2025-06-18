def solution(gems):
    answer = []
    short = len(gems) + 1   # 최단 구간 길이 설정
    l, r = 0, 0

    jewel = len(set(gems))  # gems에서 보석의 종류 찾아내기
    dic = {}

    while r < len(gems):
        if gems[r] not in dic:
            dic[gems[r]] = 1
        else:
            dic[gems[r]] += 1
        r += 1

        while len(dic) == jewel:
            if r - l < short:
                short = r - l
                answer = [l + 1, r]

            dic[gems[l]] -= 1
            if dic[gems[l]] == 0:
                del dic[gems[l]]
            l += 1

    return answer