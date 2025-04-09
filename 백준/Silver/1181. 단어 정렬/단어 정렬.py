# 1번 방법
N = int(input())

word = []
for tc in range(N):
    word.append(input())

set_word = set(word)
word_lst = list(set_word)
word_lst.sort() # 알파벳 순으로 정렬
word_lst.sort(key=lambda x: len(x))  # 정렬 기준을 단어의 길이로 바꿔서 정렬하기.

for i in word_lst:
    print(i)

# 2번 방법
N = int(input())

word = set(input() for _ in range(N))
word_lst = sorted(word, key=lambda x: (len(x), x))  # sorted(iterable, key = 정렬 기준 함수) -> 정렬된 리스트를 새로 만들어서 반환하는 함수
# 파이썬에서 튜플을 정렬하면 첫 번째 요소를 먼저 비교하고, 같으면 두 번째 요소를 비교! -> 첫 번째 기준은 문자의 길이이고, 그 다음은 단어 그 자체. 즉 알파벳 순이다.
for w in word_lst:
    print(w)
    
# 시간을 더 줄일 수 있는 방법은?
