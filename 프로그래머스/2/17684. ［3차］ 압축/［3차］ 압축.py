def solution(msg):
    dic = {chr(65 + i): i + 1 for i in range(26)}
    next_num = 27
    
    answer = []
    i = 0
    
    while i < len(msg):
        w = msg[i]  # 현재 입력
        # w를 최대한 늘려가면서 사전에 있는지 확인을 해준다.
        while i + len(w) < len(msg) and (w + msg[i + len(w)]) in dic:
            w = w + msg[i + len(w)]
        answer.append(dic[w])
        
        # 새로 등록하기
        if i + len(w) < len(msg):
            dic[w + msg[i + len(w)]] = next_num
            next_num += 1
        
        # w 길이만큼 i를 늘려주기
        i += len(w)
        
    return answer