# 뭐 속도면에서는 이게 더 좋은 풀이인듯
N = int(input())

lst = []
for i in range(1, N + 1):
    n_sum = i + sum(map(int, str(i)))
    if N == n_sum:
        lst.append(i)

if lst:
    print(lst[0])
else:
    print(0)

# 이 방법이 더 느리다!
# N = int(input())
# 
# lst = []
# for i in range(1, N + 1):
#     n_sum = i + sum(map(int, str(i)))
#     if N == n_sum:
#         print(i)
#         break
#     if i == N:
#         print(0)
