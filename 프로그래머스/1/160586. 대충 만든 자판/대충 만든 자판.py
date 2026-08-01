# 그리디를 사용을 할건데 여기서 중요한 것은 각 글자가 몇 번 눌리는지 저장을 하는 것이다.
# 저장을 하기 위해서 딕셔너리를 사용을 하기로 할 것이고 누르는 횟수를 변수로 저장하여 딕셔너리에 담아준다.
# 이때 주의할 점은 각각의 버튼에서 누르는 횟수가 더 적은 횟수가 있다는 것이다. 그렇기에 조건문을 작성을 해주는데 press < cost[ch]라는 조건문을 달아서 더 적다면 cost[ch]를 새로운 press로 업데이트를 해준다.

def solution(keymap, targets):
    cost = {}   # 몇 번 누르는지를 체크하기 위한 딕셔너리 생성
    for key in keymap:
        for i, ch in enumerate(key):
            press = i + 1   # 누르는 횟수 저장
            if ch not in cost or press < cost[ch]:
                cost[ch] = press
                
    # 각 타겟 단어 계산
    answer = []
    for target in targets:
        total = 0
        for c in target:    # target의 단어를 순회하면서 만약 그 단어가 없다면 -1로 total을 설정하고 바로 break
            if c not in cost:
                total = -1
                break
            total += cost[c]    # 그 외에는 total을 cost[c]만큼 늘려준다.
        answer.append(total)
        
    return answer