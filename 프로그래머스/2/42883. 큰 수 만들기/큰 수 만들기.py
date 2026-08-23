def solution(number, k):
    stack = []
    
    for i in number:
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
        
    if k > 0:   # 다 했음에도 k가 남아있으면 stack에서 -k 범위전까지 끊어줘야한다.
        stack = stack[:-k]
    answer = ''.join(stack)
    return answer