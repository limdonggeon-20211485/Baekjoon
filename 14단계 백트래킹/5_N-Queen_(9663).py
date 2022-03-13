# 나중에 다시 풀어보기
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀 함수 깊이의 한도를 10000까지 늘려준다 (원래 1000)

N = int(input())

answer = 0
board = [-1] * N  # 1차원 배열로도 가능 board[i] = j 의 의미는 (i, j)

def is_promising(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i): # 같은 열에 퀸이 있거나, 대각선 상에 있으면 거짓
            return False
    
    return True

def n_queens(x):
    global answer      # 함수 안에서 answer을 사용하겠다
    if x == N:
        answer += 1

    else:
        for i in range(N):
            # [x, i]에 퀸을 놓겠다.
            board[x] = i
            if is_promising(x):   # 만약 다음줄에 놓을 수 있으면 다음 줄 호출
                n_queens(x+1)

n_queens(0)
print(answer)
'''

import sys
input = sys.stdin.readline

def build_queen(x, N):
    global result     # 함수 안에서 result를 사용하겠다
    
    if x == N:         # 마지막 줄 까지 퀸을 놓았으면 result += 1
        result += 1
        return

    else:
        for i in range(N):
            row[x] = i
            for j in range(x):
                # 같은 열에 퀸이 있거나, 대각선 상에 있으면 탈출
                if row[j] == row[x] or (row[x] - x) == (row[j] - j) or (row[x] + x) == (row[j] + j): 
                    break
            # 만약 다음줄에 놓을 수 있으면 다음 줄 호출
            else:
                build_queen(x + 1, N)

N = int(input())

result = 0
row = [-1] * N  # 1차원 배열로도 가능 row[i] = j 의 의미는 (i, j)

build_queen(0, N)

print(result)