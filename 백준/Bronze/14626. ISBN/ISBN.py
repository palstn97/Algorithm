isbn = input()

for i in range(10):
    temp = isbn.replace('*', str(i))    # *을 str(i)로 대체해서 10개를 다 돌아볼 것

    total = 0
    for j in range(12): # 타입 일치 잘 시킬 것!
        if j % 2 == 0:
            total += int(temp[j])
        else:
            total += int(temp[j]) * 3

    total += int(temp[12])

    if total % 10 == 0:  
        print(i)
        break