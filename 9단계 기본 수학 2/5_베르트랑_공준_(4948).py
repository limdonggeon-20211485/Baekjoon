import sys
input = sys.stdin.readline

a = [False, False,] + [True] * ((2 * 123456) - 1)  # 소수 판 생성
primes = []

for i in range(2, (2 * 123456) + 1):     # 2 * 123456 까지 소수 판별 (에라토스테네스의 체)
    if a[i]:
        primes.append(i)
    for j in range(i, (2 * 123456) + 1, i):
        a[j] = False

while True:
    n = int(input())
    range_primes = []

    if  n == 0:
        break

    for i in primes:
        if n < i <= (2 * n):
            range_primes.append(i)

    print(len(range_primes))