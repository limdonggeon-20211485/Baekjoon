import sys
input = sys.stdin.readline

N = int(input())

number_list = []

for i in range(N):
    number_list.append(int(input()))

for i in range(len(number_list) - 1):    # 선택정렬 알고리즘, 리스트 길이의 - 1 만큼 반복
    min_idx = i
    for j in range(i + 1, len(number_list)):        # i + 1부터 리스트 길이만큼 반복
        if number_list[j] < number_list[min_idx]:   # 하나씩 대조하면서 더 작은게 나오면 작은 인덱스 바꿈 
            min_idx = j                             # 앞에서부터 차례 차례 작은게 쌓이게 됨
    number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]

for i in number_list:
    print(i)