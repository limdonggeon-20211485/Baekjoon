import sys
input = sys.stdin.readline

num = int(input())

number = 2

while num >= number:
    if num % number == 0:
        num /= number
        print(number)
    else:
        number += 1