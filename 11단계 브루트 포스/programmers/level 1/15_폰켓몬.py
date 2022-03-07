def solution(nums):
    answer = 0
    _nums = list(set(nums))
    if len(nums) / 2 > len(_nums): # 포켓몬의 종류보다 가져갈 수 있는 개수가 더 많으면 포켓몬 종류만큼 리턴
        return len(_nums)
    else:
        return int(len(nums) / 2)  # 가져갈 수 있는 개수가 포켓몬의 종류보다 적거나 같으면 가져갈 수 있는 개수 만큼 리턴

print(solution([3,3,3,2,2,2]))