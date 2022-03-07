import sys
input = sys.stdin.readline
a = int(input())
for i in range(1, a+1):
    b = '*' * i
    print('{0:>{1}}'.format(b, a))