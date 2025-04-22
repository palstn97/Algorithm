N, M = map(int, input().split())


def ma(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def mi(a, b):
    return (a * b) // ma(a, b)


print(ma(N, M))
print(mi(N, M))