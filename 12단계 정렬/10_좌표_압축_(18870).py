import sys
input = sys.stdin.readline

N = int(input())

pos_list = list(map(int, input().split()))
set_list = sorted(set(pos_list))     # 중복 제거, 정렬
new_pos_dic = {set_list[i] : i for i in range(len(set_list))}  # 요소, 바뀐 좌표(요소보다 작은 다른 요소의 수)

for i in pos_list:
    print(new_pos_dic[i], end = ' ')