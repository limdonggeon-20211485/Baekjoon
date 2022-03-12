import sys
input = sys.stdin.readline

N = int(input())

array = []

for i in range(N):
    x, y = map(int, input().split())
    array.append([x, y])

array.sort()  # 이차원 리스트도 오름차순 정렬 가능, array.sort(key=lambda x: (x[0], x[1])) 이것도 가능

for i in range(N):
    print(array[i][0], array[i][1])