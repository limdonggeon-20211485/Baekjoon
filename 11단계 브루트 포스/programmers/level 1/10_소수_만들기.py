from itertools import combinations
def solution(nums):
    all_combination = list(combinations(nums, 3))  # combination은 (1,2), (2,1) 처럼 중복 제거, permutations는 중복 제거 x
   
    sum_list = []
    for i in all_combination:  # 모든 조합의 합 구하기
        sum_list += [sum(i)]
    
    # sum_list = list(set(sum_list))  # 중복 제거(문제에서 설명을 이상하게 함, 중복제거를 하면 안된다)
    
    prime_list = []                 # 소수를 모을 리스트
    for a in sum_list:
        for b in range(2, a):   # 2부터 합 전까지
            if a % b == 0:  # 합이 2~a으로 나누었을때 나누어지면 break로 안쪽 for문 탈출
                break
        else:                # break 없이 빠져나오면 여기로
            prime_list.append(a)
    
    answer = len(prime_list)

    return answer

print(solution([1,2,7,6,4]))