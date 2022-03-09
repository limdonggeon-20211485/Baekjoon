import sys
input = sys.stdin.readline

M, N = map(int, input().split())

chess_board = []

for i in range(M):
    chess_board.append(input().rstrip())

start_point = []
for i in range((M-7)):
    for j in range((N-7)):
        start_point.append([i, j])

count_collect = []
for x, y in start_point:
    count = 0
    eight_chess_board = []
    eight_chess_board.append(chess_board[x][y:y+8])
    eight_chess_board.append(chess_board[x+1][y:y+8])
    eight_chess_board.append(chess_board[x+2][y:y+8])
    eight_chess_board.append(chess_board[x+3][y:y+8])
    eight_chess_board.append(chess_board[x+4][y:y+8])
    eight_chess_board.append(chess_board[x+5][y:y+8])
    eight_chess_board.append(chess_board[x+6][y:y+8])
    eight_chess_board.append(chess_board[x+7][y:y+8])

    for i, line in enumerate(eight_chess_board):
        for j in range(8):
            if eight_chess_board[0][0] == "B" and eight_chess_board[7][7] != "W":
                if i % 2 == 0 and j % 2 == 0:
                    if line[j] == "B":
                        pass
                    else:
                        count += 1
                
                elif i % 2 != 0 and j % 2 != 0:
                    if line[j] == "B":
                        pass
                    else:
                        count += 1
                
                elif i % 2 == 0 and j % 2 != 0:
                    if line[j] == "W":
                        pass
                    else:
                        count += 1
                
                elif i % 2 != 0 and j % 2 == 0:
                    if line[j] == "W":
                        pass
                    else:
                        count += 1

            

            elif eight_chess_board[0][0] == "W" and eight_chess_board[7][7] != "B":
                if i % 2 == 0 and j % 2 == 0:
                    if line[j] == "W":
                        pass
                    else:
                        count += 1
                
                elif i % 2 != 0 and j % 2 != 0:
                    if line[j] == "W":
                        pass
                    else:
                        count += 1
                
                elif i % 2 == 0 and j % 2 != 0:
                    if line[j] == "B":
                        pass
                    else:
                        count += 1
                
                elif i % 2 != 0 and j % 2 == 0:
                    if line[j] == "B":
                        pass
                    else:
                        count += 1



            elif eight_chess_board[0][0] == "B" and eight_chess_board[7][7] == "W":
                if i % 2 == 0 and j % 2 == 0:
                    if line[j] == "W":
                        pass
                    else:
                        count += 1
                
                elif i % 2 != 0 and j % 2 != 0:
                    if line[j] == "W":
                        pass
                    else:
                        count += 1
                
                elif i % 2 == 0 and j % 2 != 0:
                    if line[j] == "B":
                        pass
                    else:
                        count += 1
                
                elif i % 2 != 0 and j % 2 == 0:
                    if line[j] == "B":
                        pass
                    else:
                        count += 1



            elif eight_chess_board[0][0] == "W" and eight_chess_board[7][7] == "B":
                if i % 2 == 0 and j % 2 == 0:
                    if line[j] == "W":
                        pass
                    else:
                        count += 1
                
                elif i % 2 != 0 and j % 2 != 0:
                    if line[j] == "W":
                        pass
                    else:
                        count += 1
                
                elif i % 2 == 0 and j % 2 != 0:
                    if line[j] == "B":
                        pass
                    else:
                        count += 1
                
                elif i % 2 != 0 and j % 2 == 0:
                    if line[j] == "B":
                        pass
                    else:
                        count += 1
        
    count_collect.append(count)

print(min(count_collect))