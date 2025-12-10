import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1 if not stack else 0)
    elif command[0] == 'top':
        print(stack[-1] if stack else -1)