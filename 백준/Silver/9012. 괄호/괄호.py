# stack의 핵심은 LIFO, 즉 마지막에 들어간 것이 먼저 나오는 것
T = int(input())

for _ in range(T):
    S = input()
    stack = []

    for c in S:
        if c == '(':
            stack.append(c) # 여는 괄호는 push -> 무조건 스택에 넣기
        else:
            if stack:   # 스택에 뭐라도 들어있으면
                stack.pop() # 짝 맞춰서 제거해주기
            else:   # 스택에 아무 것도 없다면
                stack.append(c) # 짝이 안맞으니까 일단 집어 넣어주고
                break   # 이 경우는 종료
    print("YES" if not stack else "NO")
