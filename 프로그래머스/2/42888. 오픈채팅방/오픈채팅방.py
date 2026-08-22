def solution(record):
    nickname = {}   # 아무래도 uid랑 닉네임이랑 따로 있으니까 이걸 딕셔너리로 관리해주면 uid에 맞게 닉네임을 바로 설정할 수 있을 것이다.
    action = [] # 각각의 행동이랑 어떤 uid가 어떤 행동을 했는지 파악할 수 있는 리스트 생성
    
    for i in record:
        parts = i.split()  # 띄어쓰기를 기반으로 3개로 나누기
        # uid, nick = parts[1], parts[2] -> 처음부터 이렇게 하면 런타임 에러가 발생한다. 왜냐면 Leave의 경우에는 parts[2]가 존재하지 않기 때문이다.
        if parts[0] == "Enter":
            uid, nick = parts[1], parts[2]
            nickname[uid] = nick
            action.append((uid, "들어왔습니다."))
        elif parts[0] == "Leave":
            uid = parts[1]
            action.append((uid, "나갔습니다."))
        else:
            uid, nick = parts[1], parts[2]
            nickname[uid] = nick
    answer = []
    for n, a in action:
        answer.append(f"{nickname[n]}님이 {a}")   # f스트링 사용법 숙지해두기
    
    return answer