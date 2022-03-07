import sys
input = sys.stdin.readline
a = int(input())
b = []
for i in range(a):
    b += [list(map(int, input().split()))]
for i in b:
    count = i[0]
    total_score = 0
    c = []
    for k in i:
        total_score += k
    total_score -= count
    average = total_score/count
    for v in i:
        if v == count: continue
        if v > average:
            c += [v]
    print('{0:0.3f}%'.format((len(c)/count)*100))
