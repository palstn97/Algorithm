L = int(input())
arr = input()
r = 31
M = 1234567891
hashing = 0
for i in range(len(arr)):
    hashing += ((ord(arr[i]) - 96) * (r ** i))  # 가중치를 빼줘야하기 때문에 -96하기! 또한 아스키코드로 변환은 ord()를 사용하자
result = hashing % M
print(result)