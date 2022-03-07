import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

print(min(x, w - x, y, h - y)) 

# 왼쪽, 오른쪽 변과 x 사이의 거리, 위, 아래쪽 변과 y의 사이의 거리 중 최솟값
