import sys
from itertools import combinations
input = sys.stdin.readline
a = int(input())
b = [] #층
c = [] #호
for i in range(a):
    b += [int(input())]
    c += [int(input())]

for i in range(a):
    d = 1
    e = 1    
    if c[i] == 1:
        print(1)
        continue
    elif c[i] == 2:
        print(b[i] + 2)
        continue
    for k in range(b[i] + c[i], b[i] + c[i] -1- b[i], -1):
        d *= k
    for v in range(1, b[i] + 1 + 1):
        e *= v
    print(int(d/e))

#combination을 활용해 품
#itertools.combinations를 활용하여 할 수 있음(백준에서는 메모리 초과가 뜸)
'''
5층 : 1 7c1 8c6 9c6
4층 : 1 6c1 7c5 8c5
3층 : 1 5c1 6c4 7c4
2층 : 1 4c1 5c3 6c3
1층 : 1 3c1 4c2 5c2

대충 이런식임
'''