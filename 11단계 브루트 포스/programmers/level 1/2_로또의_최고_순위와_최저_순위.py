def solution(lottos, win_nums):
    answer = []
    if lottos.count(0) == 0:            # 0의 개수가 0일때
        win_count = 0
        for i in lottos:
            if i in win_nums:           # 당첨 번호가 있을 때마다 + 1
                win_count += 1
        if win_count == 0:              # [1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12] 처럼 같은게 하나도 없을때를 위하여
            answer += [6, 6]
        else:
            answer += [7 - win_count, 7 - win_count]
    elif lottos.count(0) == 1:           # 0의 개수가 1일때       
        win_count = 0
        for i in lottos:
            if i in win_nums:
                win_count += 1
        answer += [7 - 1- win_count, 7 - win_count]
    elif lottos.count(0) == 2:           # 0의 개수가 2일때
        win_count = 0
        for i in lottos:
            if i in win_nums:
                win_count += 1
        answer += [7 - 2- win_count, 7 - win_count]
    elif lottos.count(0) == 3:           # 0의 개수가 3일때
        win_count = 0
        for i in lottos:
            if i in win_nums:
                win_count += 1
        answer += [7 - 3- win_count, 7 - win_count]
    elif lottos.count(0) == 4:           # 0의 개수가 4일때
        win_count = 0
        for i in lottos:
            if i in win_nums:
                win_count += 1
        answer += [7 - 4- win_count, 7 - win_count]
    elif lottos.count(0) == 5:           # 0의 개수가 5일때
        win_count = 0
        for i in lottos:
            if i in win_nums:
                win_count += 1
        answer += [7 - 5- win_count, 7 - win_count]
    else:                                # 0의 개수가 6일때
        win_count = 0
        for i in lottos:
            if i in win_nums:
                win_count += 1
        answer += [1, 6]

    return answer

print(solution([1,2,3,4,5,6], [7,8,9,10,11,12]))