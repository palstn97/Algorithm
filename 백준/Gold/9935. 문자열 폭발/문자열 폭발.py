string = input().strip()
bomb = input().strip()

stack = []
bomb_len = len(bomb)

for c in string:
    stack.append(c)

    # 스택의 마지막 부분이 폭발 문자열과 같은지 확인하기 -> 스택에 폭발 문자열 길이만큼 문자가 쌓였는가?
    if len(stack) >= bomb_len:
        if ''.join(stack[-bomb_len:]) == bomb:  # stack[-bomb_len:] -> 스택의 마지막 bomb_len개 문자이다. 만약 이게 폭발 문자열과 일치한다면?
            for _ in range(bomb_len):
                stack.pop() # 폭탄 길이만큼 스택에서 빼주기! -> 후입선출이니까

if stack:
    print(''.join(stack))
else:
    print("FRULA")