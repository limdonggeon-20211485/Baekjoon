# 1.
def solution(id_list, report, k):
    answer = [0] * len(id_list)       # 정답의 리스트 요소 만큼 자리 확보(빈 리스트에서 만드는 것보다 시간 단축이라고 어디서 봤음)
    reports = {x : 0 for x in id_list}   # id마다 몇번의 신고를 받았는지에 대한 딕셔너리 틀 생성
    
    for r in set(report):          # set을 통해 중복 제거
        reports[r.split()[1]] += 1   # 그냥 split()은 공백을 기준, split에 인덱싱 가능, reports 딕셔너리에 id별로 신고 몇번 받았는지 기록 
    
    for r in set(report):
        if reports[r.split()[1]] >= k:       # 신고를 k번 이상 받았을 때
            answer[id_list.index(r.split()[0])] += 1  # 인덱싱에 맞게 1 추가

    return answer
 
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))



# 2.
def solution(id_list, report, k):
    answer = []
    a = list(set(report))                                # 중복 제거
    dictionary2 = {name : 0 for name in id_list}         
    dictionary = {name : [] for name in id_list}
    for i in a:
        dictionary[i.split()[1]].append(i.split()[0])   # 딕셔너리에 신고 당한 사람 추가

    for i in dictionary:
        if len(dictionary[i]) >= k:
            for j in dictionary[i]:
                dictionary2[j] += 1        # 신고 횟수 k번 이상이면 추가

    for i in dictionary2:
        answer.append(dictionary2[i])

    return answer



# 3.
def solution(id_list, report, k):
    answer = [0] * len(id_list)                                         # 미리 리스트 자리 확보
    dic_report = {id: [] for id in id_list}                             # 해당 유저를 신고한 ID
    for i in set(report):     # 중복 제거
        i = i.split()
        dic_report[i[1]].append(i[0])

    for key, value in dic_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1

    return answer
