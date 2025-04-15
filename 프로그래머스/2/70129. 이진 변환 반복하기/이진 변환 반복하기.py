def solution(S):
    cnt = 0
    zero = 0
    while S != '1':
        zero += S.count('0')
        S = S.replace('0', '')
        S_len = len(S)
        S = bin(S_len)[2:]
        cnt += 1

    return [cnt, zero]