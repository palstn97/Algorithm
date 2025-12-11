# queue는 선입선출 구조의 자료구조 -> 먼저 들어온 데이터가 먼저 나가는 구조
import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        q.append(int(command[1]))
    elif command[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(1 if not q else 0)
    elif command[0] == 'front':
        print(q[0] if q else -1)
    elif command[0] == 'back':
        print(q[-1] if q else -1)

'''
deque 사용하는 방법
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    command = input().split()
        if command[0] == 'push':
        q.append(int(command[1]))
    elif command[0] == 'pop':
        if q:
            print(q.popleft())  # O(1) 시간 복잡도!
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(1 if not q else 0)
    elif command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
'''