# 1.
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:  # idx = 5면 나머지0, 인덱싱 오류 안나고 순환 가능(나머지를 이용)
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):         # max 함수를 이용
            result.append(idx+1)

    return result



# 2. (위의 답과 비슷)
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p) # 정답 개수 [0,0,0]으로 설정

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]



# 3.
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),          # 리스트 무한 반복하는 함수
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:  # next는 리스트의 다음 요소를 반환(리스트 자체가 input)
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]



# 4.
