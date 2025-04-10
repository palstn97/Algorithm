while True:
    N = input()
    if N == '0':
        break
    result = 0
    for i in range(len(N)//2):
        if N[i] == N[len(N) - i - 1]:
            result += 1
    if result == len(N) // 2:
        print('yes')
    else:
        print('no')