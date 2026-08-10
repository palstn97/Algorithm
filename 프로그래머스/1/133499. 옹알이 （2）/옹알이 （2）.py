def solution(babbling):
    answer = 0
    for i in babbling:
        i = i.replace('aya', '1')
        i = i.replace('ye', '2')
        i = i.replace('woo', '3')
        i = i.replace('ma', '4')
        
        if not i.isdigit(): # 만약 다른 발음이 있다면
            continue    # 다음 단어로 넘어가기
            
        flag = True # 연속되는 문자인지 판단하는 플래그
        for j in range(len(i) - 1):
            if i[j] == i[j + 1]:
                flag = False
                break
        
        if flag:
            answer += 1
            
    return answer