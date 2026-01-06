parts = input()
# -를 기준으로 나눠서 괄호를 넣으면 최소가 되겠지?
part = parts.split('-')

result = []
for i in part:
    result.append(sum(map(int, i.split('+'))))  # +를 기준으로 part를 나누고 그 값들을 sum해준 것

sum = result[0]
for j in range(1, len(result)):
    sum -= result[j]

print(sum)