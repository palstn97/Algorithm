def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i])[2:]
        b = bin(arr2[i])[2:]
        a = '0' * (n - len(a)) + a
        b = '0' * (n - len(b)) + b
        line = ''
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                line += '#'
            elif a[j] == '0' and b[j] == '0':
                line += ' '
        answer.append(line)

    return answer