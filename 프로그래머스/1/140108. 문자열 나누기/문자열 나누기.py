def solution(s):
    answer = 0
    
    while s:
        word = s[0]
        len1 = 1
        len2 = 0
        cut = len(s)    # 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료. 이것을 해결하기 위해서 설정해둔 장치이다.
        for c in range(1, len(s)):
            if word == s[c]:
                len1 += 1
            else:
                len2 += 1
            if len1 == len2:
                cut = c + 1
                break
        s = s[cut:]
        answer += 1
        
    return answer