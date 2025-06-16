def solution(n):
    ans = 0
    num = bin(n)
    for i in range(2, len(num)):
        if num[i] == '1':
            ans += 1

    return ans