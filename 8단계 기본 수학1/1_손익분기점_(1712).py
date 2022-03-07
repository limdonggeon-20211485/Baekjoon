import sys
input = sys.stdin.readline
fixed, variable, price = map(int, input().split())
if variable >= price:
    break_even_point = -1
else:
    break_even_point = (fixed//(price-variable)) + 1
print(break_even_point)