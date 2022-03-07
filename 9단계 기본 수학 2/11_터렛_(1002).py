import sys
input = sys.stdin.readline

for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5 # 두 원의 중심 사이의 거리

    if distance == 0 and r1 == r2: # 류재명이 있을 수 있는 위치가 무한대 (둘의 원이 겹칠때)
        print(-1)                  # 두 원이 동심원이고 반지름이 같을때
    
    elif abs(r1 - r2) < distance < r1 + r2: # 두 원이 두 점에서 만날때
        print(2)
    
    elif r1 + r2 == distance or abs(r1 - r2) == distance:
        print(1)
    
    else:
        print(0)