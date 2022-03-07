import sys
input = sys.stdin.readline
a = int(input())
b = list(map(int, input().split()))
print(min(b), max(b))
