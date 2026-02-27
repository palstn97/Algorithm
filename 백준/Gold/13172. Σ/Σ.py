import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7
# 모듈러 연산에서는 소수점, 분수 표현이 불가능하다. 그래서 나누기 6 대신에 곱하기 6의 역원으로 바꾸는 것이다. 즉 1/A를 모듈려 역원이라 하고 A^(-1) mod p라고 한다.
def solution(a):
    return pow(a, MOD - 2, MOD) # pow는 파이썬 내장 함수로 거듭제곱을 계산한다. pow(a, b)는 a^b이다. pow(a, b, mod)는 a^b mod p -> 매 단계마다 mod 취하면서 계산
    # 그래서 N ^ (MOD - 2)를 계산하는데, 매 단계마다 MOD로 나눈 나머지를 취하면서 계산하라는 뜻이다.

M = int(input())
ans = 0

for _ in range(M):
    N, S = map(int, input().split())
    ans = (ans + S * solution(N)) % MOD # S/N을 모듈러로 표현해서 주사위의 기댓값을 구하고 누적한다. 그 뒤에 더할 때마다 MOD로 나눠서 숫자를 작게 유지한다.

print(ans)