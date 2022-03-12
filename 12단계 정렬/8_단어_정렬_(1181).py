import sys
input = sys.stdin.readline

N = int(input())

word_list = []

for i in range(N):
    word_list.append(input().strip())
    
word_list = list(set(word_list))

array = []

for i in word_list:
    array.append([len(i), i])

array.sort()    # [숫자, 문자] 이렇게 되있어도 자동 정렬 

for i in array:
    print(i[1])