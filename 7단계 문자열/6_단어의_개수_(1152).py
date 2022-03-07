import sys
input = sys.stdin.readline
a = input().strip()
if len(a) == 0:
    print(0)
else:
    print(a.count(' ')+1)
