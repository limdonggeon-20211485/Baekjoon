import sys
input = sys.stdin.readline
a = int(input())
for i in range(a):
    a, b = input().split()
    c = 0
    d = ''
    for x in range(len(b)):
        d += b[x]*int(a)
        c += 1
    print(d)
