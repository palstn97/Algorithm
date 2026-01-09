A, B, C = map(int, input().split())

def multiple(a, b, c):
    if b == 0:
        return 1
    
    half = multiple(a, b//2, c)
    result = (half * half) % C
    
    if b % 2 == 1:
        result = (half * half * a) % c

    return result

print(multiple(A, B, C))