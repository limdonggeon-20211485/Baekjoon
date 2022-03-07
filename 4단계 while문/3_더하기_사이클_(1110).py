import sys
input = sys.stdin.readline
a = input().rstrip()
b = a
count = 0
while True:
    if int(b) < 10:
        b = '0' + b
    c = str(int(b[0]) + int(b[1]))
    b = str(int(b[-1])) + str(int(c[-1]))
    if '0' == b[0]:
        b = b[1]
    count += 1
    if b == a:
        break
print(count)
