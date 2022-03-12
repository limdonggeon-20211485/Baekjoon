import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())

N_list = [x for x in range(1, N + 1)]

all_combination = list(permutations(N_list, M)) # combination은 (1,2), (2,1) 처럼 중복 제거, permutations는 중복 제거 x

all_combination.sort()

for i in all_combination:
    print(*i)