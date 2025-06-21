'''
전형적인 dp문제..!
연습이 더 필요
'''
T = int(input())

for _ in range(T):
    N = int(input())
    z, o = 1, 0 # 0, 1이 각각 호출된 횟수를 1, 0으로 초기화
    for i in range(N):
        z, o = o, z + o # 피보나치에 의하면 0은 1이 호출된 만큼 나오고 1은 0과 1이 호출된 것이 더해진만큼 나온다.

    print(z, o)
