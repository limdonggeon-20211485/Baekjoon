location = {
    1 : [0, 0],
    2 : [1, 0],
    3 : [2, 0],
    4 : [0, -1],
    5 : [1, -1],
    6 : [2, -1],
    7 : [0, -2],
    8 : [1, -2],
    9 : [2, -2],
    0 : [1, -3],
}
left_column = [1, 4, 7] # 왼쪽 열 숫자
right_column = [3, 6, 9] # 오른쪽 열 숫자

def solution(numbers, hand):
    answer = ''
    left_location = [0, -3]  # 현재 왼손 좌표
    right_location = [2, -3] # 현재 오른손 좌표
    for num in numbers:
        if num in left_column:                    # 왼쪽 열이면 왼손으로
            left_location = location[num]
            answer += 'L'
        elif num in right_column:                 # 오른쪽 열이면 왼손으로
            right_location = location[num]
            answer += 'R'
        else:                                     # 가운데 열일 경우
            if (abs(left_location[0] - location[num][0]) + abs(left_location[1] - location[num][1])) > \
                (abs(right_location[0] - location[num][0]) + abs(right_location[1] - location[num][1])):   # 오른손이 가까운 경우
                right_location = location[num]
                answer += 'R'
            elif (abs(left_location[0] - location[num][0]) + abs(left_location[1] - location[num][1])) < \
                (abs(right_location[0] - location[num][0]) + abs(right_location[1] - location[num][1])):   # 왼손이 가까운 경우
                left_location = location[num]
                answer += 'L'
            else:                                         # 왼손, 오른손 둘 다 거리가 같을때 어떤 손잡이인지에 따라 결정
                if hand == 'left':                    
                    left_location = location[num]
                    answer += 'L'
                else:
                    right_location = location[num]
                    answer += 'R'

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))