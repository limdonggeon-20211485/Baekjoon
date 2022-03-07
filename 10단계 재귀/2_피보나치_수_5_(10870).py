import sys
input = sys.stdin.readline

dic_f = {0 : 0, 1 : 1, 2 : 1}  # 메모제이션

def Fibonacci(n):
    if n in dic_f:
        return dic_f[n]

    dic_f[n] = Fibonacci(n - 1) + Fibonacci(n - 2)   # 메모제이션
    return dic_f[n]

print(Fibonacci(int(input())))