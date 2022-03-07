# 앞 번호 사람것을 우선적으로 지급(문제에는 나와있지 않은 조건)
def solution(n, lost, reserve):
    answer = 0
    uniform = {}
    
    for i in range(1, n+1):
        uniform[i] = 1
    
    for i in lost:
        uniform[i] -= 1
    
    for i in reserve:
        uniform[i] += 1

    for key, value in uniform.items():
        if value == 0:                            # 체육복이 없느 경우
            if key > 1 and uniform[key-1] == 2:   # 맨 처음 번호인 경우를 제외 왼쪽 번호가 여분이 있는 경우(앞 번호 사람것을 우선적으로 지금) 
                uniform[key-1] -= 1
                uniform[key] += 1
            elif key < n and uniform[key+1] == 2: # 맨 마지막 번호인 경우를 제외 오른쪽 번호가 여분이 있는 경우
                uniform[key+1] -= 1
                uniform[key] += 1

    for value in uniform.values():
        if value >= 1:
            answer += 1

    return answer

print(solution(5, [2, 4], [3, 5]))