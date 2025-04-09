N = int(input())

word = []
for tc in range(N):
    word.append(input())

set_word = set(word)
word_lst = list(set_word)
word_lst.sort()
word_lst.sort(key=len)

for i in word_lst:
    print(i)