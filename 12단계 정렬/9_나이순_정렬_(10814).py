import sys
input = sys.stdin.readline

N = int(input())

people_list = []

for i in range(N):
    people_list.append([i] + input().split())

for i in people_list:
    i[0], i[1] = int(i[1]), i[0]  # 나이와 들어온 순서의 순서를 바꿔주면서 나이를 int형으로 바꿔줌

people_list.sort()

for i in people_list:
    print(i[0], i[2])