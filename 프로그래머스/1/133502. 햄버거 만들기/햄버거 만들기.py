def solution(ingredient):
    stack = []
    pattern = [1, 2, 3, 1]
    answer = 0
    
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == pattern:
            answer += 1
            del stack[-4:]
            
    return answer