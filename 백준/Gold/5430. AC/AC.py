'''
실제로 뒤집으면 시간복잡도가 뒤집을 때마다 O(n)이 되기 때문에 터질거다.
그러면 방향만 생각해서 앞에서 뺄지, 뒤에서 뺄지만 생각하면 된다.
is_reversed라는 플래그를 사용해서 방향을 기억하자.
이때는 deque를 사용해서 앞에서 빼거나 뒤에서 빼거나를 하면 된다.
만약에 D를 만난다면 is_reversed가 False일때는 앞에서 제거하고 True일 때는 뒤에서 제거한다.
그리고 만약에 마지막에 is_reversed가 True 라면 순서를 한 번만 뒤집에 주면 끝!
'''
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input().strip()   # [1, 2, 3, 4] 또는 []와 같은 형태로 입력 받기

    if n == 0:
        q = deque()
    else:
        q = deque(arr[1:-1].split(',')) # 괄호 제거하고 쉼표로 분리해서 deque로 변환하기! -> deque(['1', '2', '3', '4']) 이런 형식일거임!

    is_reversed = False # 플래그
    error = False

    for i in p:
        if i == 'R':
            is_reversed = not is_reversed
        elif i == 'D':
            if len(q) == 0:
                error = True
                break
            if is_reversed:
                q.pop() # 뒤에서 제거하기
            else:
                q.popleft() # 앞에서 제거하기

    if error:
        print("error")
    else:
        if is_reversed:
            q.reverse()
        print('[' + ','.join(q) + ']')  # join은 리스트/deque의 요소들을 쉼표로 연결해서 하나의 문자열로 만들어준다. -> '구분자'.join(리스트나 deque)