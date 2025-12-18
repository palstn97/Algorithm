'''
이분탐색으로 접근해 보기
이분 탐색의 핵심은 범위를 절반씩 줄여가면서 찾는거다.

# 정렬된 배열에서 target 찾기
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == target:
        print(f"찾았다! 인덱스 {mid}")
        break
    elif arr[mid] < target:
        left = mid + 1  # 오른쪽 절반 탐색
    else:
        right = mid - 1  # 왼쪽 절반 탐색
```

**동작 과정:**
```
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

1단계: left=0, right=9
mid=4, arr[4]=9 > 7 → right=3

2단계: left=0, right=3
mid=1, arr[1]=3 < 7 → left=2

3단계: left=2, right=3
mid=2, arr[2]=5 < 7 → left=3

4단계: left=3, right=3
mid=3, arr[3]=7 == 7 → 찾았다!
```

## 2. 파라메트릭 서치 (Parametric Search)

### 이분 탐색의 확장 버전

**일반 이분 탐색:** 배열에서 값 찾기
**파라메트릭 서치:** **조건을 만족하는 최댓값/최솟값** 찾기

**백준 2805가 바로 이것!**

### 개념 이해
```
질문: "H 높이로 자르면 M 이상 가져갈 수 있나?"
→ YES/NO로 답할 수 있음

H = 0  → YES (많이 가져감)
H = 5  → YES
H = 10 → YES
H = 15 → YES
H = 16 → NO (적게 가져감)
H = 17 → NO
H = 20 → NO

패턴: YES YES YES YES NO NO NO
      ←─────────┘
      이 경계를 찾는 것!

범위가 크면 이분탐색을 의심해보고 먼저 떠올려 보자. 그리고 조건 만족을 yes/no로 판단이 가능하면 이분탐색을 떠올리자.

'''

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2
    wood = 0    # 가져갈 수 있는 나무

    for tree in trees:
        if mid < tree:
            wood += tree - mid
    
    if wood >= M:
        result = mid
        left = mid + 1  # H를 더 키워야지만 최솟값을 찾을 수 있다. -> mid보다 큰 값에도 조건을 만족하는 게 있는지 확인 -> 탐색 범위를 [mid + 1, right]로 줄임
    else:
        right = mid - 1 # H를 낮춰야 한다! -> 탐색 범위를 [left, mid - 1]로 줄임

print(result)