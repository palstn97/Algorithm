import sys
input = sys.stdin.readline  # 백준 문제는 입력을 이렇게 받아야한다고 한다,,,

N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))    # 입력 받은 수 lst에 append하기

lst.sort()

for num in lst:
    sys.stdout.write(str(num) + '\n')   # 출력 형식이다. 잘 알아두자.
