def solution(players, callings):
    player_dict = {}
    for i, name in enumerate(players):
        player_dict[name] = i
    
    for calling in callings:
        idx = player_dict[calling]
        prev = idx - 1  # 앞 등수의 인덱스
        players[idx], players[prev] = players[prev], players[idx]   # 두 사람의 등수 바꿔주기
        # 딕셔너리 위치도 바꿔줘야 에러 발생하지 않는다. -> swap이 일어난 시점이니까 idx, prev으로 간다.
        player_dict[players[idx]] = idx
        player_dict[players[prev]] = prev
        
    answer = []
    for p in players:
        answer.append(p)
    
    return answer