def solution(participant, completion):
    par_dic = {}                    # 딕셔너리의 자료의 접근 = O(1), 효율성 좋음
    for key in participant:         # 해시 = 파이썬에서 딕셔너리 (키, 값)                    
        if key in par_dic.keys():   
            par_dic[key] += 1       # 키 값 충돌 방지
        else:
            par_dic[key] = 1
    
    for key in completion:
        par_dic[key] -= 1

    for key in par_dic:
        if par_dic[key] > 0:
            return key


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))