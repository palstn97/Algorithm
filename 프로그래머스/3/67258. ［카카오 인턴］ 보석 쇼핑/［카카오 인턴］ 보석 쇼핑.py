def solution(gems):
    answer = []
    short = len(gems) + 1   # 최단 구간 길이 설정
    l, r = 0, 0

    jewel = len(set(gems))  # gems에서 보석의 종류 찾아내기
    dic = {}

    while r < len(gems):    # 오른쪽 포인터의 위치가 끝까지 갈때까지
        if gems[r] not in dic:  # 만약 dic에 보석이 없다면 담아주기
            dic[gems[r]] = 1
        else:
            dic[gems[r]] += 1   # 있으면 하나씩 늘려주기
        r += 1  # 포인터 한칸 이동

        while len(dic) == jewel:    # 모든 종류의 보석이 포함될때까지
            if r - l < short:   # 현재 구간의 길이가 설정한 최단 구간 길이보다 짧으면
                short = r - l
                answer = [l + 1, r] # 진열대는 1부터 시작하니까 l + 1부터 answer에 담아주기. r의 경우에는 첫 번째 while문에서 먼저 +1이 됐으므로 그대로 r로 저장

            dic[gems[l]] -= 1   # 최소 구간을 찾아야 하니까 해당하는 보석 하나 줄이기
            if dic[gems[l]] == 0:   # 만약 보석의 개수가 0이라면 아예 그 보석을 삭제하기 -> 두 번째 while문의 조건에 맞지 않으니까 탈출
                del dic[gems[l]]
            l += 1  # 왼쪽 포인터 한 칸 옮기기

    return answer


# 다른 방법
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
