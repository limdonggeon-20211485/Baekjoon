def solution(absolutes, signs):
    answer = 0
    for num, sign in enumerate(signs):
        if sign:
            answer += absolutes[num]
        else:
            answer -= absolutes[num]
               
    return answer

print(solution([4,7,12], [True,False,True]))