words = [input() for _ in range(3)]

for i in range(3):
    if words[i].isdigit():  # isdigit() -> 문자열이 모두 숫자로만 이루어져 있으면 True
        num = int(words[i])
        next_word = num + (3 - i)   # 그냥 무조건 +1을 하면 안됨
        break   # 숫자 찾으면 바로 종료

if next_word % 3 == 0 and next_word % 5 == 0:
    print('FizzBuzz')
elif next_word % 3 == 0:
    print('Fizz')
elif next_word % 5 == 0:
    print('Buzz')
else:
    print(next_word)