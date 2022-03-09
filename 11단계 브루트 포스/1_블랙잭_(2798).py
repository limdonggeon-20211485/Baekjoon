import sys
from itertools import combinations
input = sys.stdin.readline

N, maximum = map(int, input().split())

number = list(map(int, input().split()))

answer = 0

for i in combinations(number, 3):            # 모든 nc3 경우의 수 구하기
    candidate = sum(i)                
    if candidate > maximum:                         # 맥시멈 값보다 크면 탈락
        continue

    if answer <= candidate:                         # 현재까지 있던 정답보다 크면 정답을 바꿈
        answer = candidate

print(answer)