# 1. (지금은 정렬안하면 18, 20 통과 X)
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost] # 여분이 있는 사람중에 도난 안 당한 사람만 추가
    _lost = [l for l in lost if l not in reserve]    # 여분이 없는 사람중에 도난 당한 사람만 추가
    for r in _reserve:
        f = r - 1     # 여분 있는 사람의 앞 번호 
        b = r + 1     # 여분 있는 사람의 뒷 번호
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)



# 2. (지금은 13 통과 X)
def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer