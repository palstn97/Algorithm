N = int(input())

member = []

# key 매개변수를 가지는 sort() -> key값을 기준으로 정렬되고 기본값은 오름차순
# lambda 식을 사용 할 수 있다. -> 그렇기에 두 개의 조건으로 정렬할 때는 이것을 사용

for i in range(N):
    age, name = input().split()
    member.append((int(age), name))
# 1.
member.sort(key=lambda x: x[0])
for j in member:
    # 처음에는 member.sort(key=lambda x: x[0])으로 했는데 nonetype은 iterable하지 않다고 함 -> sort()는 반환값이 none이니까
    print(j[0], j[1])

# 2.
for j in sorted(member, key=lambda x: x[0]):
    print(j[0], j[1])
