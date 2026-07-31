def solution(s, skip, index):
    # 알파벳리스트를 만든다. 기본적으로 a부터 z까지를 만드는데 만약에 skip에 있으면 빼줘야 하니 if를 사용하여 제거!
    alphabet_list = [chr(i) for i in range(ord('a'), (ord('z') + 1)) if chr(i) not in skip]
    n = len(alphabet_list)
    answer = ''
    
    for i in s:
        j = alphabet_list.index(i)  # i의 인덱스가 몇 인지 파악 -> .index()를 사용해주자.
        new_j = (j + index) %  n   # j + index의 새로운 인덱스 설정, 그리고 z넘어가면 다시 a로 가야하니 alphabet_list 길이만큼 나눈 나머지로 인덱스 설정
        answer += alphabet_list[new_j]
    return answer