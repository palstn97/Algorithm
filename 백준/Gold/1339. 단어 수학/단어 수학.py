N = int(input())
words = []
for _ in range(N):
    words.append(input())

weights = {}

for w in words:
    l = len(w)
    for i, c in enumerate(w):
        v = 10 ** (l - i - 1)
        if c in weights:
            weights[c] += v
        else:
            weights[c] = v

sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)

num = 9
total = 0
for c, w in sorted_weights:
    total += w * num
    num -= 1

print(total)