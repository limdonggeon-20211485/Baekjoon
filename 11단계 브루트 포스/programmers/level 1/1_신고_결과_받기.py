def solution(id_list, report, k):
    # 한 유저의 중복 신고 제거
    deduplication_report = list(set(report))   
    
    reporter = []
    reported = []
    for i in deduplication_report:
        report_temp = i.split(" ")
        reporter.append(report_temp[0])    # 신고자 분류
        reported.append(report_temp[1])    # 신고 당한 사람 분류

    dic = {} 
    for m in id_list:
        count = reported.count(m)   
        if count >= k: # 신고 횟수가 k 번 이상
            dic[m] = count # id = key, 신고 당한 횟수 = value
    
    # 누가 누구를 신고했는지 딕셔너리 작성 (중복 키 피하기 위해서 값을 리스트로)
    dic2 = {}                                           
    for i in range(len(reporter)):
        if reporter[i] not in dic2.keys():
            dic2[reporter[i]] = [reported[i]]
        else:
            dic2[reporter[i]] += [reported[i]]
    
    # 각 신고자가 얼마나 메일 받아야 하는지 작성
    dic3 = {}
    for k in dic.keys():
        for key, value in dic2.items():
            if k in value:
                if key not in dic3.keys():
                    dic3[key] = 1               
                else:
                    dic3[key] += 1

    
    answer = []
    for i in id_list:
        if i in dic3.keys():
            answer.append(dic3[i])
        else:
            answer.append(0)    # dic3에 키가 없으면 0을 추가
        
           
    return answer
 

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))