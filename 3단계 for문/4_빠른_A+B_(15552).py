import sys

a = int(sys.stdin.readline())
for i in range(a):
    m, n = map(int, sys.stdin.readline().split())
    print(m+n)
