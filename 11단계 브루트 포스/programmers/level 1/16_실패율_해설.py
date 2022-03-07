# 1.(내 코드 최적화 버전, 내 코드에서 카운터를 쓰면 더욱더 최적화 가능)
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)  # 정렬 기준은 값으로



# 2.
def solution(N, stages):
    fail = {}
    for i in range(1,N+1):
        try:
            fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i]) # 이런식으로도 가능하구나..
        except:
            fail_ = 0
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True)
    return answer



# 3.
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:  # 여기서 카운트 함수를 안써서 시간 복잡도 감소
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer
