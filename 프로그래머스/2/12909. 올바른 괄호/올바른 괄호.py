def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()

    if len(stack) == 0: # stack의 길이가 0이면 True 반환
        return True
    else:
        return False