def solution(board, moves):
    answer = 0
    basket = []
    for num in moves:
        for i in board:
            if i[num-1] != 0:                 # 0이 아니면(인형이 있으면)
                basket.append(i[num-1])       # 인형을 바스켓에 옮기고
                i[num-1] = 0                  # 인형이 없어진 자리에 0 채워넣기
                break                         # 찾으면 안 쪽 for문 탈출
    
    count = 0  # 삭제가 되면 인덱싱이 밀리는 것을 방지 + 삭제되고 앞 뒤가 또 똑같은 상황을 방지(삭제 될때마다 2씩 증가)
    for i in range(len(basket)):  # 바구니에 1개만 있으면  인덱싱 오류나는 것을 방지
        if len(basket) > 1:
            if i-count == 0: # basket 맨 처음 2개가 삭제되면 인덱싱 오류 나는 것을 방지
                pass
            elif basket[i-1-count] == basket[i-count]:
                del basket[i-1-count]
                del basket[i-1-count]   # 앞에 먼저 지워져서 -1을 추가로 빼서 인덱싱
                count += 2
                answer += 2
               
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
