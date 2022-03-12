import sys
input = sys.stdin.readline

N = input().strip()

array = []

for i in N:
    array.append(int(i))

array.sort(reverse=True)

answer = ''

for i in array:
    answer += str(i)

print(answer)