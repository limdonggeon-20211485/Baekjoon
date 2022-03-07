import sys
input = sys.stdin.readline
a, b = map(int, input().split())
a = str(a)
b = str(b)
c = ''
d = ''
for i in range(len(a)):
    c += a[-1-i]
for i in range(len(b)):
    d += b[-1-i]
c = int(c)
d = int(d)
if c > d:
    print(c)
else:
    print(d)
