def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5] * ((len(answers)//5) + 1)                    # 5마다 반복 이므로 answers의 길이가 5의배수일 때마다 더해줌
    two = [2, 1, 2, 3, 2, 4, 2, 5] * ((len(answers)//8) + 1)           # 위의 이유로 8배수마다 더해줌
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((len(answers)//10) + 1)  # 위의 이유로 10배수마다 더해줌
    
    result_dic = {1 : 0, 2 : 0 , 3 : 0}          
    
    for i in range(len(answers)):
        if one[i] == answers[i]:
            result_dic[1] += 1
        if two[i] == answers[i]:
            result_dic[2] += 1
        if three[i] == answers[i]:
            result_dic[3] += 1
    print(result_dic)

    for i in range(1, len(result_dic.items()) + 1):
        if i == 1:
            answer.append(i)
            continue
        if result_dic[answer[-1]] > result_dic[i]:
            continue
        elif result_dic[answer[-1]] < result_dic[i]:
            answer = [i]
        else:
            answer.append(i)

    return answer

print(solution([1,3,2,4,2]))