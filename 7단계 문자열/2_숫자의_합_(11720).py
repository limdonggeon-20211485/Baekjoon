import sys
input = sys.stdin.readline
a = int(input())
b = input().rstrip()
c = 0
for i in b:
    c += int(i)
print(c)
