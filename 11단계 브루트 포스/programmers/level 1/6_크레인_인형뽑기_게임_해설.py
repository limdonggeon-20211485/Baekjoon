# 1.
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:                     # 요소가 1개가 넘어야함(인덱싱 오류 방지)
                    if stacklist[-1] == stacklist[-2]:     # 인덱싱 오류 방지하기 위해서 
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer



# 2.
def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board))) 
    # *로 리스트 한 번 unpacking 하고 집 
    # map을 이용해 나누어진 행들에 lambda를 적용
    # 첫번째 lambda의 조건으로 또 lambda를 쓴다
    a, s = 0, [0]                           # a는 떠뜨려진 인형의 수, s는 바스켓, [0]을 넣은것은 pop을 썼을때 오류 방지용
   
    for m in moves:
        if len(cols[m - 1]) > 0:                                # 행에 인형이 있으면
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):     # := <- 일부러 변수에 값을 대입하는 것, 행의 젤 위의 인형과 바스켓의 젤 마지막 인형과 비교
                a += 2
            else:
                s.extend([l, d])      # 아니라면 아까 if 조건문에서 pop으로 빠졌기 때문에 원래 있던 l을 추가하고 다음으로 d를 새로 추가한다

    return a
