from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

N_list = [x for x in range(1, N + 1)]

all_combination = list(combinations_with_replacement(N_list, M)) # 중복 조합, M자리는 N_list를 몇 번 반복 할건지
all_combination.sort()                                           # product의 repeat와 똑같은 것 같음

for i in all_combination:
    print(*i)