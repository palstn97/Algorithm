'''
greedy로 풀어봅시다.
5개의 광물 단위로 쪼개고 각각의 피로도를 돌 곡괭이를 기준으로 풀어보자.
그리고 정렬을 해서 가장 피로도가 높은 녀석을 다이아 곡괭이 부터 배정을 하면 될듯!
'''
def solution(picks, minerals):
    # 1. 실제로 캘 수 있는 광물 개수만큼 자르기
    total_pick = sum(picks)
    minerals = minerals[:total_pick * 5]    # 곡괭이 1개당 5개씩 캘 수 있으니까 minerals 재정의

    # 2. 광물을 5개씩 묶어서 각 구간의 난이도 계산하기! -> 이건 돌 곡괭이 기준으로
    groups = []
    for i in range(0, len(minerals), 5):
        group = minerals[i:i + 5]
        level = 0
        for mineral in group:
            if mineral == 'diamond':
                level += 25
            elif mineral == 'iron':
                level += 5
            else:
                level += 1

        groups.append((level, group))
        # groups = [(난이도1, [광물 5개]), (난이도2, [광물 5개]), ...]

        # 3. 난이도가 높은 구간을 앞으로 정렬하기
        groups.sort(reverse=True)

        answer = 0
        # 각각의 곡괭이 갯수
        dia_pick = picks[0]
        iron_pick = picks[1]
        stone_pick = picks[2]

        for level, group in groups:
            if dia_pick > 0:
                for mineral in group:
                    if mineral == 'diamond':
                        answer += 1
                    elif mineral == 'iron':
                        answer += 1
                    else:
                        answer += 1
                dia_pick -= 1
            
            # 다이아 곡괭이가 없으면 철 곡괭이 사용
            elif iron_pick > 0:
                for mineral in group:
                    if mineral == 'diamond':
                        answer += 5
                    elif mineral == 'iron':
                        answer += 1
                    else:
                        answer += 1
                iron_pick -= 1
            
            else:
                for mineral in group:
                    if mineral == 'diamond':
                        answer += 25
                    elif mineral == 'iron':
                        answer += 5
                    else:
                        answer += 1
                stone_pick -= 1

    return answer