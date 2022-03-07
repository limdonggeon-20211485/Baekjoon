import sys
input = sys.stdin.readline

primes = [False, False,] + [True] * (10000 - 1)  

for i in range(2, 101):     # n의 소수 판별 최대 약수가 루트(n) 이하이므로 101까지 (여기서 n의 최댓값 10000)
    if primes[i]:
        for j in range(i + i, 10000 + 1, i):
            primes[j] = False

for i in range(int(input())):
    n = int(input())

    A = n//2   # n의 절반
    B = A

    for i in range(10000):
        if primes[A] and primes[B]:
            print(A, B)
            break
        A -= 1   # A, B에 각각 1을 빼고 더해주면서 값을 찾음
        B += 1
        


        

                
        
   
