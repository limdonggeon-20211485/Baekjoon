import sys
input = sys.stdin.readline
a = int(input())
b = 7                    #3번째 방까지 가기 위한 최소 개수
c = 6                    #늘어나는 규칙이 6의 배수로 늘어남.
x = 2                    #방 지나는 개수(기본 값 2개로 설정)
y = 2                    #다음 방을 건너기 위한 개수 2배 곱해 줌.  
if a == 1:
    print(1)
else:
    while a > b:
        x += 1
        b = b + (c * y)
        y += 1
    print(x)

# 방을 지날 때 1, 6, 12, 18, 씩 가야함. 즉, 다음 방을 가려면 이전에 방을 가기 위한 것보다 2배 더 가야함.