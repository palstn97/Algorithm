S = input()
result = [-1] * 26  # a ~ z에 대응하는 26개

for i, char in enumerate(S):
    idx = ord(char) - ord('a')  # a = 0, b = 1, ... , z = 25
    if result[idx] == -1:
        result[idx] = i

print(*result)

# find() 사용하기 -> 처음 등장 위치를 반환하고 없으면 -1 반환
# S = input()
# for char in 'abcdefghijklmnopqrstuvwxyz':
#     print(S.find(char), end = ' ')
