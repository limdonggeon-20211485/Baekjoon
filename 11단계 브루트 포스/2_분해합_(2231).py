import sys
input = sys.stdin.readline

N = int(input())
_min = N

for i in range(N):    # 0부터 N까지
    _sum = i
    for j in str(i):    # 생성자 구하기
        _sum += int(j)
    if _sum == N:
        if _min >= _sum:  # 생성자 중에서 작은 것 구하기
            _min = i

if _min == 1 or _min == N:   # N이 1이거나 값이 없으면 0 출력
    print(0)
else:
    print(_min)