def solution(numbers):
    answer = 0
    for num in range(10):
        if not num in numbers:    # 숫자가 numbers에 없으면 answer에 그 숫자를 더하기
            answer += num

    return answer

print(solution([5,8,4,0,6,7,9]))