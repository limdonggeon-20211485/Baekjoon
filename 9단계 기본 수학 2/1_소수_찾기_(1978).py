import sys
input = sys.stdin.readline

count = int(input())
lst = list(map(int, input().split()))

for i in lst:
    if i == 1:
        count -= 1
        continue
    elif i == 2:
        continue
    for l in range(2, i):
        if i % l == 0:
            count -= 1
            break

print(count)


    


