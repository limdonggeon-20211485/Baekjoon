import re    # 정규 표현식 import
# 1.
def solution(new_id):
    st = new_id
    st = st.lower()                            # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.     
    st = re.sub('[^a-z0-9\-_.]', '', st)       # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    # +는 1개 이상 의미, '.'은 어떤값이든 받는것, \.쓰면 .으로 인식 
    st = re.sub('\.+', '.', st)                # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다. 
    st = re.sub('^[.]|[.]$', '', st)           # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    st = 'a' if len(st) == 0 else st[:15]      # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    st = re.sub('^[.]|[.]$', '', st)           # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
                                               # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])  # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    return st



# 2.
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer
