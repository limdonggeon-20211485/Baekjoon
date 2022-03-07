import operator
def solution(N, stages):
    count_dic = {}
    pro_dic = {}

    for num in range(1, N + 1):
        count_dic[num] = stages.count(num)
    
    den = len(stages)  # 분모
    for num in range(1, N + 1):
        if count_dic[num] != 0:
            pro_dic[num] = count_dic[num] / den
            den -= count_dic[num]                 # 다음 분모는 전 분모에서 전 분자를 뺀 것
        else:
            pro_dic[num] = 0                      # 이렇게 안하면 런타임 에러남 (이유는 모르겠음...)
    
    pro_dic = sorted(pro_dic.items(), key=operator.itemgetter(1), reverse=True)  # 기존의 순서를 유지하면서 값을 기준으로 정렬
                                                                                 # a = {1:1, 4:1, 2:1, 3:1}를 이렇게 하면 
    return [x[0] for x in pro_dic]                                               # [(1, 1), (4, 1), (2, 1), (3, 1)] 이렇게 됌
                                                                                 # 여기서는 키를 순서대로 해놔서 가능
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))