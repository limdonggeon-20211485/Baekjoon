import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())

N_list = [x for x in range(1, N + 1)]

all_combination = list(product(N_list, repeat = M)) # 중복 순열 repeat는 N_list를 몇 번 반복할건지 2면 [x , y] 이렇게 담김

all_combination.sort()

for i in all_combination:
    print(*i)