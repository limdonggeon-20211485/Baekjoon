# 1.
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]      # 순위 설정

    cnt_0 = lottos.count(0)   # lottos에서 0의 개수          
    ans = 0
    for x in win_nums:         
        if x in lottos:       # lottos에 당첨 번호가 있을 때 마다 ans에 1추가
            ans += 1
    return [rank[cnt_0 + ans],rank[ans]]    

print(solution([1,2,3,4,5,6], [7,8,9,10,11,12]))



# 2.
def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]



# 3.
def solution(lottos, win_nums):
    zero = lottos.count(0)
    a= [x for x in lottos if x in win_nums]   # win_nums랑 맞으면 a에 추가
    max = zero+len(a)
    min = len(a)

    max = 7- max if max >=1 else 6     # max가 0, 즉 일치하는게 없으면 6
    min = 7- min if min >=1 else 6     # min이 0, 즉 일치하는게 없으면 6
    return [max,min]
