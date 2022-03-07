import sys
input = sys.stdin.readline
a = int(input())
if a == 4 or a == 7:     #4와 7은 안 되므로 -1 출력
    print(-1)
else:
    count = 0
    while True:
        if a % 5 == 0:              
            count += a//5
            break
        else:
            a -= 3                          #5로 나누어 질 때 까지 3을 빼다가 5로 나누어지면 5로 나눔
            count += 1
    print(count)

'''
4와 7은 안된다.
8, 9, 10이 되므로
11이상의 것들은 모두 된다.(8, 9 ,10에서 3만 더하면 무조건 된다.)
''' 