import sys
input = sys.stdin.readline

people = []
N =int(input())

for i in range(N):
    people.append(list(map(int, input().split())))

people_rank = [1] * N    # 등수 리스트를 미리 만들어 놓기

for person in range(N):
    for num in range(N):
        if people[person][0] < people[num][0] and people[person][1] < people[num][1]:  # 사람의 키와 몸무게 각각 비교
            people_rank[person] += 1

print(*people_rank)   # *를 이용해 리스트 풀어주기