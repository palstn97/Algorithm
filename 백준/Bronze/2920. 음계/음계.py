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