import sys
input = sys.stdin.readline
a = []
for i in range(9):
    a += [int(input())]
print(max(a))
k = 1
for i in a:
    if i == max(a):
        print(k)
    k += 1
