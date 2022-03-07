import sys
input = sys.stdin.readline

n = int(input())
Map = [[0 for i in range(n)] for i in range(n)]

def star(n):
    global Map
    
    if n == 3 :                              # n이 3일 경우엔 기본 프리셋 리턴
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return

    a = n//3
    star(n//3)                       # n이9일 때
    for i in range(3):               # a*i+k는 행 번호 반복문 돌리면 차례대로 0,1,2,3,4,5,6,7,8 행 선택
        for j in range(3) :          # a*j:a*(j+1)는 0:3, 3:6, 6:9 이렇게 열 선택
            if i == 1 and j == 1 :   # i == 1, j == 1 일때는 가운데 공백에 해당 
                continue
            for k in range(a) :
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]
          
star(n)

for i in Map :
    for j in i :
        if j :
            print('*', end = '')     # 1이면 별 찍기
        else :                       # 0이면 공백
            print(' ', end = '')
    print()                          # 한 줄 적으면 줄 바꿈