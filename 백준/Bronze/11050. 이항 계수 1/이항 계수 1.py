import math
N, K = map(int, input().split())

result = (math.factorial(N)) / ((math.factorial(N - K)) * (math.factorial(K)))

print(int(result))