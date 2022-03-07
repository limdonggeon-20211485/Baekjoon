import sys
input = sys.stdin.readline
a = int(input())
b = []
for x in range(a):
    b += [input().rstrip()]
c = []
for x in b:
    for y in x:
        if x.find(y * x.count(y)) == -1:     #그룹 단어가 아닌 것 구하기
            if x not in c:
                c += [x] 
print(len(b)-len(c))