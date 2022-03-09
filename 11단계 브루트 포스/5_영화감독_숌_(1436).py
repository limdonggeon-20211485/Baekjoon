import sys
input = sys.stdin.readline

N = int(input())
count = 666      # N번째 영화 제목에 들어갈 숫자를 찾을 때 까지 계속 1씩 올라감
series = 0       # 666이 포함된 시리즈 갯수, 순서대로 올라감

while True:
    if '666' in str(count):
        series += 1
        if series == N:
            print(count)
            break

    count += 1