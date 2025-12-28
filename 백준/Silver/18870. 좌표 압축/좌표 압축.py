import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

# 정렬하고 중복을 제거해야 하니까 sorted 사용하고 lst를 set에 담아주기
# 이때 sorted()는 새로운 리스트를 반환하고 원본이 변경되지 않는다. 반면에 .sort()는 반환값이 없고 원본이 변경된다.
lst2 = sorted(set(lst))

# 나보다 작은 값을 찾아야하는데 이걸 간단하게 랭킹이라고 생각하면 됨. 0순위라면 나보다 큰 수가 0이라는 뜻!
# 이때 enumerate를 사용해서 딕셔너리를 만들것! enumerate는 인덱스와 값을 동시에 가져오는 것이다. (인덱스, 값) 이렇게 가져옴
# 딕셔너리로 반환하는 건 rank[value] = idx
# 딕셔너리 컴프리헨션을 사용하기
rank = {value: idx for idx, value in enumerate(lst2)}

print(' '.join(str(rank[x]) for x in lst))
