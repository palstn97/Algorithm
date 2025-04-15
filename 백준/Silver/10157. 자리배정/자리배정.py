C, R = map(int, input().split())

K = int(input())

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction = 0
arr = [[0] * C for _ in range(R)]
cnt = 1
curr_r = (R - 1)
curr_c = 0
arr[curr_r][curr_c] = cnt

while cnt < K:
    if K > C * R:
        break

    next_r = curr_r + dir[direction][0]
    next_c = curr_c + dir[direction][1]
    if 0 <= next_r < R and 0 <= next_c < C and arr[next_r][next_c] == 0:
        cnt += 1
        arr[next_r][next_c] = cnt
        curr_r, curr_c = next_r, next_c
    else:
        direction = (direction + 1) % 4

if K > C * R:
    print(0)
else:
    print(curr_c + 1, R - curr_r)