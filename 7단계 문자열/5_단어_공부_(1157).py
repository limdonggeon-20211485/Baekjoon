import sys
input = sys.stdin.readline
a = input().rstrip()
a = a.upper()
b = set(a)
b = list(b)
b.sort()
c = []
d = []
for i in range(len(b)):
    c += [a.count(b[i])]
    d += [a.count(b[i])]
c.sort()
if len(c) >= 2:
    if c[-1] == c[-2]:                   #가장 많이 사용된 알파벳이 2개 이상이면 ? 출력
        print('?')
    else:
     print(b[d.index(c[-1])])            #c는 정렬을 했음. c에서 최대 사용 개수가 d의 어디 위치에 있는지 하고 b에서 추출 ex) b = [a,b,c]
else:                                    #                                                                               d = [3,2,4]
    print(b[d.index(c[-1])])             #면 a 3번, b 2번, c 4번
