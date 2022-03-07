# 1. (내 답의 최적화 버전)
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):        # combinations 랑 똑같음
        cand = sum(a)
        for j in range(2, cand):  # 2부터 합 전까지
            if cand%j==0:         # 2~합 전까지의 수 중 하나라도 나누어지면 break
                break
        else:                  # break 없이 빠져나오면 여기로
            answer += 1
    return answer



# 2. 
from itertools import combinations      
def prime_number(x):      
    answer = 0                             # **0.5는 루트와 같은 의미
    for i in range(1,int(x**0.5)+1):       # 소수 판정법 중에 가장 알려진 예시 하나가 주어진 자연수 n에 대해서 1보다 크고 
        if x%i==0:                         # 루트 n 이하인 모든 자연수들로 나누어떨어지지 않으면 소수라는 것
            answer+=1
    return 1 if answer==1 else 0                                   

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])