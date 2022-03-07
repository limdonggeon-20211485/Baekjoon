import sys
input = sys.stdin.readline
a = int(input())
def d(x):
    b = 0
    for x in range(1, x+1):
        if x < 100:                                                   #1, 10의 자리 숫자는 전부 한수(어떤 양의 정수 X의 각 자리가 등차수열)
            b += 1
        elif x < 1000:                                                #100의 자리 숫자는 100의 자리 숫자-10의 자리 숫자 == 10의 자리 숫자-1의 자리 숫자로 계산
            if (x//100) - ((x//10)%10) == ((x//10)%10) - (x%10):
                b += 1
    return b
c = d(a)
print(c)
