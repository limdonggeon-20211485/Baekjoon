import sys
input = sys.stdin.readline

N = int(input())

array = [0] * 10001 # 입력값이 10000이 최대므로 10001개 만들어줌

for i in range(N):   # 숫자의 빈도수 체크
    array[int(input())] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)

# 여기선 메모리 때문에 이중 포문을 썻지만
# 원래 카운팅 정렬은 시간 복잡도가 O(N) 임...