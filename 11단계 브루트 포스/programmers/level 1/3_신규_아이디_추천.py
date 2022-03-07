def solution(new_id):
    answer = ''
    
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id_1 = new_id.lower()
    

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    possible_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']    
    new_id_2 = ''
    for i in new_id_1:
        if not i.islower() and not i in possible_list:  
            pass
        else:
            new_id_2 += i
    

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    new_id_3 = ''
    for num, i in enumerate(new_id_2):
        if num == 0:
            pass
        if new_id_2[num-1] == '.' and new_id_2[num] == '.':
            pass
        else:
            new_id_3 += i
    
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id_4 = ''
    if new_id_3:  # id가 공백일 경우를 위하여            
        if new_id_3[0] == '.' and new_id_3[-1] == '.':
            new_id_4 += new_id_3[1 : len(new_id_3) - 1]
        elif new_id_3[0] == '.' and not new_id_3[-1] == '.':
            new_id_4 += new_id_3[1 : len(new_id_3)]
        elif not new_id_3[0] == '.' and new_id_3[-1] == '.':
            new_id_4 += new_id_3[0 : len(new_id_3) - 1]
        else:
            new_id_4 = new_id_3

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    new_id_5 = ''
    if new_id_4 == '':
        new_id_5 +='a'
    else:
        new_id_5 = new_id_4

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    new_id_6_1 = ''
    new_id_6_2 = ''
    if len(new_id_5) >= 16:
        new_id_6_1 += new_id_5[0 : 15]
        if new_id_6_1[0] == '.' and new_id_6_1[-1] == '.':
            new_id_6_2 += new_id_6_1[1 : len(new_id_6_1) - 1]
        elif new_id_6_1[0] == '.' and not new_id_6_1[-1] == '.':
            new_id_6_2 += new_id_6_1[1 : len(new_id_6_1)]
        elif not new_id_6_1[0] == '.' and new_id_6_1[-1] == '.':
            new_id_6_2 += new_id_6_1[0 : len(new_id_6_1) - 1]
        else:
            new_id_6_2 = new_id_6_1
    else:
        new_id_6_2 = new_id_5
    
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    new_id_7 = ''
    if len(new_id_6_2) <= 2:
        new_id_7 += new_id_6_2
        while len(new_id_7) < 3:
            new_id_7 += new_id_6_2[-1]
    else:
        new_id_7 = new_id_6_2
    
    answer = new_id_7
    
    return answer

print(solution("123_.def"))