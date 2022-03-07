import sys
input = sys.stdin.readline

while True:
    side = list(map(int, input().split()))

    if sum(side) == 0:
        break

    max_num = max(side)
    side.remove(max_num)

    if pow(max_num, 2) == pow(side[0], 2) + pow(side[1], 2):
        print('right')
    else:    
        print('wrong')