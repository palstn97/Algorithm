A = int(input())
B = int(input())
C = int(input())

num = str(A * B * C)

res = [0] * 10
for i in range(len(num)):
    res[int(num[i])] += 1

for j in range(10):
    print(res[j])

'''
다른 풀이로는 다음과 같은 풀이가 있다. -> 다만 속도는 같다. 단지 코드가 짧아진다랑 count함수를 사용한다는 것만 다를 뿐
A = int(input())
B = int(input())
C = int(input())

num = str(A * B * C)
for i in range(10):
    print(num.count(str(i)))
'''
