import sys
input = sys.stdin.readline

N = int(input())

number_list = []

for i in range(N):
    number_list.append(int(input()))

number_list.sort()
length = len(number_list)
count_dic = {}
count_max_dic = {}

average = sum(number_list) / length 
if average >= int(average) + 0.5 or average <= int(average) - 0.5:
    if average >= 0:
        print(int(average) + 1)
    else:
        print(int(average) - 1)
else:
    print(int(average)) # 산술평균



print(number_list[(length // 2)]) # 중앙값(N이 홀수기 때문에)



for i in number_list:
    if i in count_dic.keys():
        count_dic[i] += 1
    else:
        count_dic[i] = 1

for key, value in count_dic.items():
    if max(count_dic.values()) == value:
        count_max_dic[key] = value

if len(count_max_dic) == 1:
    print(*list(count_max_dic.keys()))
else:
    for num, key in enumerate(count_max_dic.keys()):
        if num == 1:
            print(key)
            break                               # 최빈값



print(max(number_list) - min(number_list))   # 범위