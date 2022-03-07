import sys
input = sys.stdin.readline

a, b = map(int, input().split())

for m in range(a, b + 1):
    if m == 1:
        continue
    elif m == 2:
        print(2)
        continue
    for n in range(2,int(m**0.5)+1):       
        if m % n == 0:
            break
    else:
        print(m)