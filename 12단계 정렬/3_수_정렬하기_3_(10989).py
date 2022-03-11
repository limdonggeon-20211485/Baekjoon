import sys
input = sys.stdin.readline

N = int(input())

number_list = []

for i in range(N):
    number_list.append(int(input()))

array = [0] * (len(number_list) + 1) # number_list 길이 + 1 만큼 숫자의 빈도수를 담을 리스트 생성

for i in number_list:   # 숫자의 빈도수 체크
    array[i] += 1

array = array[1:]   # 앞에 0 자리 제거

for i in range(1, max(number_list) + 1):  
    count = array[i-1]      # 0자리 없애서 인덱스 에러 안나게 인덱스를 한 칸씩 당겨줌
    for j in range(count):
        print(i)