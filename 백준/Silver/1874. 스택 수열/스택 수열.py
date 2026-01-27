import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
current = 1 # 다음에 push할 숫자로 1부터 시작한다. 이때 한 번 지나간 숫자는 다시 push 하지 못한다.

for _ in range(n):
    target = int(input())
    while current <= target:    # 타겟까지 도달하기 위해 필요한 숫자들을 모두 push하고자 한다. 만약에 조건에 맞지 않으면 이미 그 전의 숫자를 지나갔기 때문에 while 문을 실행하지 않는다.
        # current가 target보다 작으면 target까지 쭉 push하고 current가 target보다 크면 이미 target을 지나쳤기 때문에 while을 실행하지 않는다.
        stack.append(current)
        result.append('+')
        current += 1

    if stack and stack[-1] == target:   # stack이 비어있지 않고 가장 위에 있는게 target과 같은지 확인하기 -> 같으면 pop이 가능하고 다르면 pop이 불가능하다.
        stack.pop()
        result.append('-')

# 삼항 연산자로 A if 조건 else B -> 조건이 참이면 A 출력하고 조건이 거짓이면 B를 출력한다. -> 스택이 비어있으면 성공적으로 수열이 만들어진 것!
print('\n'.join(result) if not stack else "NO")