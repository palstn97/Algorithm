# 1번 방법
A, B, V = map(int, input().split())

day = (V - B - 1) // (A - B) + 1

print(day)

# 2번 방법
A, B, V = map(int, input().split())

if (V - A) % (A - B) != 0 :
    day = (V - A) // (A - B) + 1 + 1
else:
    day = (V - A) // (A - B) + 1


print(day)
