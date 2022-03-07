import sys
input = sys.stdin.readline
a = []
for i in range(10):
    a += [int(input())]
b = []
for i in a:
    b += [i%42]
b.sort()
c = []
for i in b:
    if c and i in c:
        continue
    c += [i]

print(len(c))
