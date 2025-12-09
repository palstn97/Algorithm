music = list(map(int, input().split()))
s = 0
for i in range(len(music) - 1):
    if music[i] == music[i + 1] - 1:
        s += 1
    elif music[i] == music[i + 1] + 1:
        s -= 1
    else:
        s += 0

if s == 7:
    print("ascending")
elif s == -7:
    print("descending")
else:
    print("mixed")

'''
이 풀이는 너무 직관적이지 못하다. 그래서 아래와 같은 풀이가 좀 더 직관적이고 괜찮을거 같다. 물론 효율 측면에서는 괜찮아 보이지만.
music = list(map(int, input().split()))

if music == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif music == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else:
    print("mixed")
'''
