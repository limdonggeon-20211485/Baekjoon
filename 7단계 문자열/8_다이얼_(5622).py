import sys
input = sys.stdin.readline
a = input().rstrip()
b = 0
for x in a:
    if x == 1:
        b += 2
    elif x in 'ABC':
        b += 3
    elif x in 'DEF':
        b += 4
    elif x in 'GHI':
        b += 5
    elif x in 'JKL':
        b += 6
    elif x in 'MNO':
        b += 7
    elif x in 'PQRS':
        b += 8
    elif x in 'TUV':
        b += 9
    elif x in 'WXYZ':
        b += 10
print(b)
