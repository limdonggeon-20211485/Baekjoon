# 1.
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion) # 요소의 갯수 세고, 카운터끼리 빼기 가능
    return list(answer.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))



# 2.
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part    # hash는 무작위의 긴 숫자가 나옴, 그 숫자가 배열의 인덱스를 정함(key값이 됌)
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer



# 3.
def solution(participant, completion):
    participant.sort()  # 정렬
    completion.sort()   # 정렬
    for i in range(len(completion)):
        if participant[i] != completion[i]: # 중간에 불일치 하는 값이 있으면 리턴
            return participant[i]
    return participant[len(participant)-1]  # 없으면 마지막값이 답



# 4.
def solution(participant, completion):   # 3번의 변형
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]



# 5.
def solution(participant, completion):
    participant_set = set(participant)    # 중복 제거
    completion_set = set(completion)      # 중복 제거
    result = list(participant_set - completion_set)  # set 자료형은 빼기 가능
    if result !=[]:                # 리설트에 값이 있다면(못 들어온 사람이 동명이인이 아니라면, 만약 중복 제거에서 제거 당해서 리스트가 비게 됨)
        return result[0]           # 1번째 값 리턴
    else:                          # 그렇지 않다면(못 들어온 사람이 동명이인이라면)
        for c in completion:       
            a=completion.count(c)  
            b=participant.count(c)
            if(a != b):
                return c
    return None



# 6.
result = {}

def solution(participant, completion):
    for a in participant:
        result[a] = result.get(a, 0) + 1   # 키 값이 없어 디폴트 값을 대신 가져오게 하고 싶을 때, get(x, default)
                                           # 여기서는 값이 없으면 0 + 1, 있으면 + 1
    for b in completion:
        result[b] -= 1
        if result[b] == 0:
            del result[b]
    return list(result.keys())[0]