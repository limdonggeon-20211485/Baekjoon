import sys
input = sys.stdin.readline

x_coor = []
y_coor = []

for i in range(3):
    coor = list(map(int, input().split()))
    x_coor.append(coor[0])
    y_coor.append(coor[1])

x_answer = 0
y_answer = 0

for x, y in zip(x_coor, y_coor):
    if x_coor.count(x) == 1:        # 5 5, 5 7, 7 5 가 주어젔으면 
        x_answer = x                # x좌표 7하나 밖에 없고, y좌표 7하나 밖에 없고 따라서 7 7이 필요
    if y_coor.count(y) == 1:
        y_answer = y

print(x_answer, y_answer)
        


