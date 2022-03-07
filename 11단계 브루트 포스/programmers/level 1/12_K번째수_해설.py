# 1.
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))



# 2.
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command             # 각각 변수 지정
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer   