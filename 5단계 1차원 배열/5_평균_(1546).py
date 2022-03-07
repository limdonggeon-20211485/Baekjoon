import sys
input = sys.stdin.readline
a = int(input())
b = list(map(int, input().split()))
b.sort()
maximum = b[-1]
c = []
for i in b:
    c += [(i/maximum)*100]
d = 0
for i in c:
    d += i
print(d/a)
