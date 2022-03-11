import sys
input = sys.stdin.readline

M, N = map(int, input().split())

chess_board = []

for i in range(M):
    chess_board.append(input().rstrip())

start_point = []
for i in range((M-7)):                # 가능한 시작지점 모으기
    for j in range((N-7)):
        start_point.append([i, j])

count_collect = []

for x, y in start_point:
    count_1 = 0
    count_2 = 0
    
    eight_chess_board = []
    eight_chess_board.append(chess_board[x][y:y+8])     # 8*8 체스판 새로 생성(시작 지점에서 0~8씩 더해서 했어도 될듯)
    eight_chess_board.append(chess_board[x+1][y:y+8])
    eight_chess_board.append(chess_board[x+2][y:y+8])
    eight_chess_board.append(chess_board[x+3][y:y+8])
    eight_chess_board.append(chess_board[x+4][y:y+8])
    eight_chess_board.append(chess_board[x+5][y:y+8])
    eight_chess_board.append(chess_board[x+6][y:y+8])
    eight_chess_board.append(chess_board[x+7][y:y+8])

    for i, line in enumerate(eight_chess_board):
        for j in range(8):
            if (i + j) % 2 == 0:
                if line[j] != 'W': count_1 += 1     # W로 시작했을 때 칠해야 할 부분
                if line[j] != 'B': count_2 += 1     # B로 시작했을 때 칠해야 할 부분
            else :
                if line[j] != 'B': count_1 += 1     # W로 시작했을 때 칠해야 할 부분
                if line[j] != 'W': count_2 += 1     # B로 시작했을 때 칠해야 할 부분
    
    count_collect.append(count_1)
    count_collect.append(count_2)

print(min(count_collect))