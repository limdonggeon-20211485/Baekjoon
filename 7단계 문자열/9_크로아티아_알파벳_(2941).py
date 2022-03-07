import sys
input = sys.stdin.readline
a = input().rstrip()
a = a.replace('c=', ' ')
a = a.replace('c-', ' ')
a = a.replace('dz=', ' ')
a = a.replace('d-', ' ')
a = a.replace('lj', ' ')
a = a.replace('nj', ' ')
a = a.replace('s=', ' ')
a = a.replace('z=', ' ')
b = len(a)
print(b)