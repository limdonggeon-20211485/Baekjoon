import re

num_dic = {'zero':'0', "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    # 정규식 re.sub(), 문자열이 모두 바뀔때까지 실행
    for key, value in num_dic.items():
        s = re.sub(key, value, s)
    
    answer = int(s)
    return answer

print(solution("123"))