T = int(input())

for tc in range(1, T + 1):
    S = input()
    stack = []
    cnt = 0
    for i in S:
        if i == '(':
            while stack:
                stack.pop()
            stack.append(i)
        elif i == '|':
            if stack and stack.pop() == '(':
                cnt += 1
            else:
                stack.append(i)
        elif i == ')':
            if stack and stack.pop():
                cnt += 1

    print(f"#{tc} {cnt}")