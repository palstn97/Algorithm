def solution(ingredient):
    stack = []
    pattern = [1, 2, 3, 1]  # 패턴이 정해져있기 때문에 패턴을 만들어주고 이거랑 비교를 하면 되겠다.
    # 이런 문제가 나오면 뒤에서부터 보면서 패턴과 비교를 하면 된다고 생각하자.
    answer = 0
    
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == pattern:   # stack의 길이가 4이상이고 뒤에서부터 확인을 했을 때, 즉 하나의 온전한 패턴을 뒤에서부터 확인을 할 때 패턴과 동일하다면 그건 햄버거를 만드는 것과 동일한 것이다.
            answer += 1
            del stack[-4:]  # 처음에는 stack = stack[:-4]로 했는데 이렇게 하니 완전히 새로운 리스트를 만들기에 시간초과가 발생한다. 그래서 간단하게 마지막 4개 원소만 제거하는 방식으로 del을 사용해주면 된다.
            
    return answer
