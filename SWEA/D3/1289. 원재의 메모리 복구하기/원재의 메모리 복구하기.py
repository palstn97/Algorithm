T = int(input())

for tc in range(1, T + 1):
    N = input()
    memory = []
    for i in N:
        memory.append(i)
    first = ['0'] * len(N)
    count = 0
    while first != memory:
        for j in range(len(N)):
            if memory[j] != first[j]:
                if first[j] == '0':
                    for k in range(j, len(N)):
                        first[k] = '1'
                    count += 1
                else:
                    for p in range(j, len(N)):
                        first[p] = '0'
                    count += 1
    print(f"#{tc} {count}")