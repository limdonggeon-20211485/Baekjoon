# 1.
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer



# 2.
def solution(numbers, hand):
    l = 10
    r = 11
    answer = ""
    p = [[0, 4, 3, 4, 3, 2, 3, 2, 1, 2],
         [4, 0, 1, 2, 0, 2, 3, 0, 3, 4],
         [3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
         [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
         [3, 0, 2, 3, 0, 1, 2, 0, 2, 3],
         [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
         [3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
         [2, 0, 3, 4, 0, 2, 3, 0, 1, 2],
         [1, 3, 2, 3, 2, 1, 2, 1, 0, 1],
         [2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
         [1, 0, 4, 5, 0, 3, 4, 0, 2, 3],
         [1, 5, 4, 0, 4, 3, 0, 3, 2, 0]]
    for i in numbers:
        if i in [1, 4, 7]:
            l = i
            answer += "L"
        elif i in [3, 6, 9]:
            r = i
            answer += "R"
        else:
            if p[l][i] < p[r][i]:
                l = i
                answer += "L"
            elif p[l][i] > p[r][i]:
                r = i
                answer += "R"
            elif hand == "left":
                l = i
                answer += "L"
            else:
                r = i
                answer += "R"
    return answer

