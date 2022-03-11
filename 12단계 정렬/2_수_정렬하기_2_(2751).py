import sys
input = sys.stdin.readline

N = int(input())

number_list = []

for i in range(N):
    number_list.append(int(input()))

number_list.sort()

for i in number_list:
    print(i)