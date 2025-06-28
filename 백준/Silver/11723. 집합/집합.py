import sys

M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    cal = sys.stdin.readline().strip().split()    # input()을 받아오는 양이 많아서 이 문제에서 는 이 방법을 사용해야 한다. 잘 알아두기. 나중에 또 이런 경우가 생길시 사용할 방법
    if cal[0] == 'add':
        S.add(int(cal[1]))
    elif cal[0] == 'remove':
        S.discard(int(cal[1]))  # discard()를 사용할 때 요소가 없으면 그냥 넘어간다. -> remove()는 없다면 오류가 발생하게 된다.
    elif cal[0] == 'check':
        if int(cal[1]) in S:
            print(1)
        else:
            print(0)
    elif cal[0] == 'toggle':
        if int(cal[1]) in S:
            S.remove(int(cal[1]))
        else:
            S.add(int(cal[1]))
    elif cal[0] == 'all':
        S = set(range(1, 21))
    elif cal[0] == 'empty':
        S.clear()
