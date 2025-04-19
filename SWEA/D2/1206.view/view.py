def view(array):
    view_sum = 0
    for i in range(2, N - 2):
        if array[i] > max(array[i - 2], array[i - 1], array[i + 1], array[i + 2]):
            view_sum += array[i] - max(array[i - 2], array[i - 1], array[i + 1], array[i + 2])

    return view_sum


for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f"#{tc} {view(arr)}")
