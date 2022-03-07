import sys
input = sys.stdin.readline
a = int(input())
b = int(input())

prime_number = []

for i in range(a, b + 1):
    if i == 1:
        continue
    elif i == 2:
        prime_number.append(i)
        continue
    for l in range(2, i):
        if i % l == 0:
            break
    else:
        prime_number.append(i)
if prime_number:
    print(sum(prime_number))
    print(min(prime_number))
else:
    print(-1)