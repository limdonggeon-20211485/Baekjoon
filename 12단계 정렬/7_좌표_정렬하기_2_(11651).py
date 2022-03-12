import sys
input = sys.stdin.readline

N = int(input())

array = []

for i in range(N):
    x, y = map(int, input().split())
    array.append([x, y])

array.sort(key=lambda x: (x[1], x[0]))   # y좌표 먼저 , x 좌표 나중

for i in range(N):
    print(array[i][0], array[i][1])