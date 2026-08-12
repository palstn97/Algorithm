def solution(survey, choices):
    # 각 유형에 맞는 점수를 저장하는 딕셔너리를 생성
    personality = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    score = [0, 3, 2, 1, 0, 1, 2, 3]    # 각각의 점수
    
    # choices의 점수를 바탕으로 4점 이상이라면 survey의 두 번째 유형에 그 만큼의 점수를 더해주고 그것이 아니라면 survey의 첫 번째 유형에 그 만큼의 점수를 더해준다.
    for i in range(len(choices)):
        choice = choices[i]
        if choice >= 4:
            target1 = survey[i][1]
            personality[target1] += score[choice]
        elif choice < 4:
            target2 = survey[i][0]
            personality[target2] += score[choice]
            
    type = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')] # 각각은 2개의 타입으로 묶여져 있다.
    
    answer = ''
    for first, second in type:  # 묶여진 두 개의 타입의 점수를 비교해서 더 큰 값을 answer에 담아준다.
            if personality[first] >= personality[second]:
                answer += first
            else:
                answer += second
            
    return answer