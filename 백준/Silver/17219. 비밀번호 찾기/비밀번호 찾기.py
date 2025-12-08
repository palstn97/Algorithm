N, M = map(int, input().split())
# 2개의 정보니까 딕셔너리를 생각해야함
password = {}

for i in range(N):
    site, pw = input().split()
    password[site] = pw # 각각의 사이트에 맞게 비밀번호 딕셔너리에 저장

for j in range(M):
    site = input()
    print(password[site])