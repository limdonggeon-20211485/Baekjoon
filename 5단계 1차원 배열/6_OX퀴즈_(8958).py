import sys
input = sys.stdin.readline
a = int(input())
b = []
for i in range(a):
    b += [input().rstrip()]
for i in b:
    score = 0
    number = 1
    for k in i:
        if k == 'O':
            score += number
            number += 1
        if k == 'X':
            number = 1
    print(score)
